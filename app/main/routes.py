from flask import make_response, request, abort, current_app
import openai
from app import session
from app.models import Question
from app.main import bp


client = openai.OpenAI()


#### Set default parameters for OpenAI model 
DEFAULT_MODEL = "gpt-3.5-turbo-instruct"
MAX_TOKENS = 255
MAX_TEMPERATURE = 0.5


### endpoint to handle POST requests for asking a question.
@bp.route('/ask', methods=['POST'])
def ask_question():
    
    try: ### extract and clean the question from the request
        question = (request.get_json()).get('question').strip()
    except:
        current_app.logger.info(f'500 HTTPException due to JSON structure. \nrequest.get_json() = {request.get_json()}')
        return abort(500, 'Error: Check your payload structure. Payload must be JSON type compatible with the structure: { "question": "<your_question>" } (without obliques)')
    

    ## validate the question, should be non empty and more than one word
    if (len(question[:-1].strip().split()) <= 1) or (not question): 
        current_app.logger.info(f'400 HTTPException due to bad question. \nrequest.get_json() = {request.get_json()}')
        return abort(400, "Error: Question must contain at least 2 words")    
    
    
    ## Create a response using OpenAI's model
    response = client.completions.create( 
        model = DEFAULT_MODEL,
        prompt = question,
        max_tokens = MAX_TOKENS,
        temperature = MAX_TEMPERATURE
    )

    answer = response.choices[0].text.strip() # extract the answer from the response

    ## create a new question object and store it in the database
    new_question = Question(question = question, answer = answer) 
    session.add(new_question)
    session.commit()
    
    # return ans store the newly created question and answer as a JSON response
    current_app.logger.info(f'The newly answered question has been successfully stored. \nThe question = {question}, \nThe model answer: {answer}')
    return make_response(new_question.__repr__(), 201) 