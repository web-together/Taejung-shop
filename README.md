## 클론 코딩 과정

- 코드 동작 과정 이해하며 직접 손으로 쳐 봅니다.
- 이해 가지 않는 부분을 체크합니다.
- 전체적인 개념이 이해 안간다 -> 수업 / 해당 주제 포스팅
- 한 두줄 정도가 이해 안간다 -> 주석 달기


## Preview

 - django==2.2.8
 - 생략 한 부분 : `6.3` RDS 설정, `6.4` S3 미디어설정

## 1주차

 - `6.5` shop 앱 만들기 부터
 - `6.6` 소셜 로그인 추가 까지

### Useful Model Columns

### Slug

#### 개념 

URL의 이름을 모델 내의 객체를 기반으로 짓는 방법

> https://web-together.github.io/ 의 12번 째 post의 제목이 Hello World 였다면?

 - https://web-together.github.io/post/12 (id)
 - https://web-together.github.io/post/Hello%20World (str)
 - https://web-together.github.io/post/Hello-World   (slug)

#### code 

```
models.py/
    slug = models.SlugField(max_length=200, db_index=True, unique=True, allow_unicode=True)
    # max_length    = slug의 최대 길이
    # db_index      = 해당 필드를 인덱스 값으로 지정
    # allow_unicode = (한글 지원) 영문을 제외한 다른 언어도 사용할 수 있게 한다

```

```
    urls.py/
    path('<slug:category_slug>/', product_in_category, name='product_in_category'),
```

---

original source = https://github.com/Baepeu/onlineshop
