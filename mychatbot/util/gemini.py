import google.generativeai as genai


# import PIL.Image

# img = PIL.Image.open('img.jpeg')

def give_desc(img):
    genai.configure(api_key='AIzaSyA8Jn6cFDCoaH6TNLyvOQvKck7fXxJkrNg')
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(img)
    return response.text

# print(give_desc(img))
