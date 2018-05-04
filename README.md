# North Korea New Year's Speechs

This repository contains the raw speech transcripts of North Korea, from 1946 to 2015.

## Data description

Each file contains the original transcript of a particular year as follows:

```
$ head 2002.txt
위대한 수령님 탄생 90돐을 맞는 올해를 강성대국건설의 새로운 비약의 해로 빛내이자


<로동신문>，<조선인민군>，<청년전위>　공동사설 - 2002년 01월 01일
해 제

공동사설은 2002년을 '위대한 수령, 위대한 영도자의 역사와 업적을 끝없이빛내기 위한 총돌격의 해, 강성대국 건설의 새로운 비약의 해'라고 규정하고  `4대 제일주의(우리 수령ㆍ우리 사상ㆍ우리 군대ㆍ우리 제도 제일주의)'를제시하며 이를 철저히 구현할 것을 강조했다.

공동사설은 또 과학기술과 교육사업 발전을 국가차원의 관심을 돌려야 한다면서 정보기술과 정보산업 발전에 전력을 쏟고 과학기술 인재 양성에 힘쓰는 한편 시급을 요하는 분야부터 공업 기술개선과 현대화사업에 추진해 나갈것을 강조했다.
```

Run `code/tokenize.py` to get a filtered list of morphemes:

```
$ head ../data/2002_tokenized.txt
위대 수령 탄생 돐 맞 올해 강성 대국 건설 비약 해 빛 내이 자 동신 문 조선 인민군 청년 전위 공동 사설 년 월 일 해 제 공동 사설 년 위대 수령 위대 영도자 역사 업적 끝없이 빛내 기 총돌격 해 강성 대국 건설 비약 해 규정 대 제일주의 우리 수령 ㆍ 우리 사상 ㆍ 우리 군대 ㆍ 우리 제도 제일주의제시 이 철저히 구현 것 강조
공동 사설 또 과학 기술 교육 사업 발전 국가 차원 관심 돌려야 한다 정보 기술 정보 산업 발전 전력 쏟 과학 기술 인재 양성 힘쓰 한편 시급 요하 분야 공업 기술 개선 현대 사업 추진 것 강조
특히 대남 분야 관련 온 민족 우리 민족 조국 통일 자주 통일 구호 높이 치켜들 모든 것 민족 이익 복종 사대 외세 존 배격 민족 공조 실현 한다고 강조 주적 포기 국가 보안법 폐지 외세 공조 포기 공동 선언 말살 시도 배격 등 촉구
원 문 오늘 우리 앙양 정치 분위기 전 민족 환희 속 새해 주체 년 뜻 깊 맞이
력사 영광 계승 위대 전도 양양 것 하 조선혁명 새 시대 진군 길 더욱 것 되 있
위대 령도 김정일 동지 서 세기 혁명 년 대 오늘 무한대 열정 투지 우리 혁명 정력 이끌 나가
지금 전체 당원 인민군 장병 인민 김정일 동지 령도 강성 대국 휘황 앞날 내 보 새해 총 진군 힘차 다그쳐 굳 결의 넘쳐 있
지난해 주체 년 세기 사회주의 강성 대국 건설 진격 가 력 사 해 이
우리 고난 행군 승리 불굴 기세 새 세기 첫해 전투 빛나 장식 였
사회주의 붉 기 고수 기 거창 투쟁 속 조선혁명 앙양기 맞이 되 였
```

## License

<p xmlns:dct="http://purl.org/dc/terms/">
  <a rel="license"
     href="http://creativecommons.org/publicdomain/zero/1.0/">
    <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
  </a>
</p>

When referencing this dataset please cite [this paper](http://www.dbpia.co.kr/Journal/ArticleDetail/NODE06388044):

```
@article{tensor2tensor,
  author    = {Jonghee Park and Eunjeong Park and Dong-joon Jo},
  title     = {Automated Text Analysis of North Korean New Year Addresses, 1946-2015},
  journal   = {Korean political science review},
  volume    = {49},
  issue     = {2},
  year      = {2015}
}
```
