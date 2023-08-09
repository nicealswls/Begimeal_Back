# 베지밀 회원가입 API 테스트 방법
## 회원가입
http://localhost:8000/users/register 로 POST 합니다.

이때 Body 예시는 다음과 같습니다.


```
{
    "username": "testuser",
    "email": "test@test.com",
    "phone_number": "010-1111-1111",
    "password": "test5678"
}
```
Send시 받는값은 다음과 같습니다.

```
{
    "user": {
        "email": "test@test.com",
        "username": "testuser",
        "phone_number": "010-1111-1111",
        "token": "JWT토큰"
    }
}
```
만약 테스트 중이라면 토큰이 나중에 쓰이므로 미리 복사해둬야 합니다.

## 로그인
회원가입이 잘 되었는지 확인용입니다.
http://localhost:8000/users/login 로 POST 합니다.

이때 Body 예시는 다음과 같습니다.


```
{
    "email": "test@test.com",
    "password": "test5678"
}
```
Send시 받는값은 다음과 같습니다.
```
{
    "user": {
        "email": "test@test.com",
        "username": "testuser",
        "last_login": "2023-08-07 16:21:52.252854+00:00"
    }
}
```


## 회원 수정
회원 정보 조회, 수정, 탈퇴 등의 기능이 있습니다.

주소는 http://localhost:8000/users/current 입니다.

그리고 Headers는 다음과 같습니다.


| Key | Value |
| --- | --- |
| Authorization | token abcdefg|

Value는 `token (토큰)` 으로 입력해야 합니다.

### 회원 정보 조회
Body는 필요 없습니다.

GET을 보내면 받는값은 다음과 같습니다.


```
{
    "user": {
        "email": "test@test.com",
        "username": "testuser",
        "token": "토큰"
    }
}
```

### 회원 정보 수정
Body 예제는 다음과 같습니다.

```
{
    "username": "testuser2",
    "email": "test2@test.com"
}
```
PATCH를 보내면 받는값은 다음과 같습니다.

```
{
    "user": {
        "email": "test2@test.com",
        "username": "testuser2",
        "token": "토큰"
    }
}
```
닉네임과 이메일이 변경되었습니다.

### 회원 탈퇴

Body는 필요 없습니다.

DELETE를 보내면 받는값은 다음과 같습니다.


```
{
    "user": {
        "result": "ok"
    }
}
```
이후 로그인 등 기타 요청시 받는값은 다음과 같습니다.


```
{
    "errors": {
        "error": [
            "A user with this email and password was not found"
        ]
    }
}
```
