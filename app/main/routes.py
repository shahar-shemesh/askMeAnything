from flask import jsonify, make_response, request, abort
import openai
from app import session
from app.models import Question
from app.main import bp


@bp.route('/test', methods=['GET'])
def test():
    return make_response(jsonify({'message': 'test route'}), 200)
    


client = openai.OpenAI() # Initialize OpenAI client


#### Set default parameters for OpenAI model 
DEFAULT_MODEL = "gpt-3.5-turbo-instruct"
MAX_TOKENS = 255
MAX_TEMPERATURE = 0.5


### endpoint to handle POST requests for asking a question.
@bp.route('/ask', methods=['POST'])
def ask_question():
    
    question = (request.get_json()).get('question').strip()     ### extract and clean the question from the request
    
    ## question[:-1].strip().split() ===> Validate the question, it should be non-empty and have more than one word
    if (len(question[:-1].strip().split()) <= 1) or (not question): 
        return abort(400, "Invalid question")    
    
    
    
    
    ## Create a response using OpenAI's model
    response = client.completions.create( 
        model = DEFAULT_MODEL,
        prompt = question,
        max_tokens = MAX_TOKENS,
        temperature = MAX_TEMPERATURE
    )

    answer = response.choices[0].text.strip() # extract the answer from the response
    
    try:
        ## tring to create a new question object and save it to the database
        new_question = Question(question = question, answer = answer) 
        session.add(new_question)
        session.commit()
        return make_response(new_question.__repr__(), 201) # return the newly created question and answer as a JSON response

    except:
        return abort(500, "Error, try another question.")