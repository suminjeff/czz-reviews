import config
import openai


def analyze_review(review):
    client = openai.OpenAI(api_key=config.OPEN_API_KEY)
    messages = [
        {
            "role": "system",
            "content": "너는 치지직이라는 네이버 웹 서비스의 리뷰에 담긴 고객 감정을 분석하고 탐지하는 AI 언어모델이야.",
        },
        {
            "role": "system",
            "content": f"다음 제품 리뷰를 분석해 고객 감정이 긍정인지 부정인지 판단해 알려줘. 대답은 다른 추가적인 설명없이 '긍정' 혹은 '부정' 둘 중 하나의 단어로 대답해야 해: {review}",
        },
    ]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=3,
        n=1,
        stop=None,
        temperature=0,
    )
    response = completion.choices[0].message.content
    return response


print(analyze_review("좋아"))
