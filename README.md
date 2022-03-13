# Online Welcome-kit

> 한국외국어대학교 글로벌캠퍼스 10기를 위한 웰컴키트입니다.

<details>
<summary> <a href=https://gooseulbyul.tistory.com/68>웰컴키트는</a> </summary>

1. 기업(브랜드)의 아이덴티티를 보여줄 수 있고 - 기업문화와 가치
2. 입사자에게 입사를 환영한다는 환영의 메시지를 전달할 수 있고
3. 업무에 필요한 다이어리와 펜 등 기본 사무용품(필요 용품)을 전달할 수 있는 등 신입사원에게 우리 기업에 대해 알려줄 수 있는 한편, 앞으로 우리 기업의 구성원이 되었다는 소속감을 강하게 심어줄 수 있는 효과적인 문화입니다.

</details>

## :tiger:멋사의 웰컴키트는

> 비전공자의 개발자 문화 적응을 돕고, 비대면 활동의 한계를 해소하기 위한 소속감 부여를 목표로 합니다.

1. 외대멋사의 가치: 협력, 공유
2. 환영의 메시지: 개별 관심사에 따른 아티클, 운영진 롤링페이퍼 제공
3. 사무용품 대신 1년동안 사용할 수 있는 도장판을 제시: 지속적 활동 격려, issue를 일상적으로 사용하며 github의 협업 기능 적응

## :heavy_check_mark: TODO's

### 디자인

- [x] **통일성 있는 컴포넌트** : figma의 template
- [x] 빙고판과 도장 : [issue #2](https://github.com/hufslion10th/welcome_kit/issues/2)

### 컨텐츠: issue에서 기록

- (우선) 합격자 선정
- 공통내용
  - [x] 아기사자로 살아남기 내용 보충 [issue #3](https://github.com/hufslion10th/welcome_kit/issues/3)
- 개별내용
  - [ ] 합격자 관심분야 파악 (데이터, 프론트, UIUX, 창업 등)
  - [ ] 관심사별 분류 후 동료 매칭: OOO님의 동료를 찾아보세요
  - [x] ~~아티클 및 도서 탐색~~ -> Project Lion: road map
  - [ ] 운영진 롤링페이퍼: 분량 균일하게

### 개발

- 정적 페이지이므로 프론트 개발만 필요

  - 축하 애니메이션: 환영페이지
  - POP UP: 롤링페이퍼
  - 레이아웃에 따른 구현: figma

- 배포: github page
  - 회원별로 폴더 하나씩, 링크 하나씩 배정

<details>
<summary>directory tree </summary>

```
- (root) hufslion10th/welcome-kit
  + 템플릿/
    - 환영 페이지
    - 웰컴키트
      + 멋사 빙고 (공통)
      + 아기사자로 살아남기 (공통)
      + 아지트 소개 (공통)
      + 운영진 메시지 (개별)
      + 동료 찾기 (개별)
  + 김멋사 /
    + 템플릿 활용해서 개별 내용만 보충
  + 박멋사 /
    + 상동
```

</details>

## :sparkles: 작업 현황

- Figma: [open link](https://www.figma.com/file/MVxwXPWDwvbjmx9x2k36z1/%EB%A9%8B%EC%82%AC10%EA%B8%B0-%EC%98%A8%EB%9D%BC%EC%9D%B8-%EC%9B%B0%EC%BB%B4%ED%82%A4%ED%8A%B8?node-id=0%3A1)
- Figma Prototype: [open link](https://www.figma.com/proto/MVxwXPWDwvbjmx9x2k36z1/%EB%A9%8B%EC%82%AC10%EA%B8%B0-%EC%98%A8%EB%9D%BC%EC%9D%B8-%EC%9B%B0%EC%BB%B4%ED%82%A4%ED%8A%B8?page-id=0%3A1&node-id=181%3A700&viewport=241%2C48%2C0.49&scaling=min-zoom&starting-point-node-id=181%3A700)

## :key: How to Use

- 협업규칙 : [issue #1](https://github.com/hufslion10th/welcome_kit/issues/1)
- 규칙은 필요에 따라 추가
