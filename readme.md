# 운동 및 식단 블로그

* 운동루틴 및 식단의 기록 및 한달 종합 인증을 위한 서비스

## WBS

* 데이터베이스 스키마 및 중요 변수
    * users
        * id : 
        * username : 

* URL
|url|||

/                           # 메인
/blog/                      # 블로그 리스트
/blog/create/               # 블로그 작성
/blog/update/<int:pk>/      # 로그인한 사용자만 보기 가능, 자신의 글만 업데이트 가능.(자신의 글에서 수정하기 버튼 노출)
/blog/delete/<int:pk>/      # 로그인한 사용자만 보기 가능, 자신의 글만 삭제 가능.(자신의 글에서 삭제하기 버튼 노출)
/blog/category              # 카테고리
/blog/category/<str:tag>/   # 해당 카테고리가 달린 목록을 가져와야 합니다.
/blog/?q='keyword'          # 해당 키워드가 포함된 title, content가 있는 목록을 가져와야 합니다.
/accounts/signup/           # 회원가입
/accounts/login/            # 로그인
/accounts/logout/           # 로그인한 사용자만 보기 가능
/accounts/profile/          # 로그인한 사용자만 보기 가능

* 와이어프레임
|메인화면||
|카테고리화면||
|포스트화면||

* 작동이미지
