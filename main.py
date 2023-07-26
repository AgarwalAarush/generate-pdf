from engine.yt_summarizer import YoutubeSummarizer
import functions_framework

@functions_framework.http
def generate_pdf(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    
    # Check for video id parameter
    if not request.args or 'viid' not in request.args:
        exit()

    # Retrieve Video ID and Construct Video URL
    video_id = request.args.get('viid')
    video_url = "https://www.youtube.com/watch?v=" + video_id

    # Apply Youtube Summarizer Object
    yts = YoutubeSummarizer()
    yts.create_document(video_url)

    # request_json = request.get_json()
    # if request.args and 'message' in request.args:
    #     return request.args.get('message')
    # elif request_json and 'message' in request_json:
    #     return request_json['message']
    # else:
    #     return f'Hello World!'