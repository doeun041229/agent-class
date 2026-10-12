# 에이전트 수업 실습 폴더

Claude Code를 활용한 **AI 에이전트 수업** 실습용 작업 공간입니다.
Claude Code의 프로젝트 설정(CLAUDE.md, 훅, MCP 서버)을 다뤄 보고, 에이전트로 만든 결과물을 모아 둡니다.

## 폴더 구성

| 경로 | 설명 |
| --- | --- |
| `.claude/CLAUDE.md` | 프로젝트 지침. Claude가 "에이전트 수업용 도우미"로 동작하게 하고, 개발 환경(GitHub CLI 설치·인증 상태)을 기록 |
| `.claude/settings.json` | Claude Code 프로젝트 설정 (프로젝트 MCP 서버 자동 활성화) |
| `.claude/hooks/ppyong.js` | `UserPromptSubmit` 훅 예제. 프롬프트에 "뿅"이 들어가면 응답 끝에 `빵빵 <현재 시각>`을 붙이도록 지시를 주입 |
| `.mcp.json` | MCP 서버 설정. [blender-mcp](https://github.com/ahujasid/blender-mcp)로 Claude가 Blender를 제어 |
| `make_cover.py` | Pillow로 인스타그램 카드뉴스 표지(1080×1350)를 만드는 스크립트 |
| `cover_ai_trend.png` | `make_cover.py`로 생성한 "AI 트렌드" 표지 이미지 |

## 실습 내용

1. **CLAUDE.md** – 프로젝트별 지침으로 에이전트의 역할과 맥락 지정
2. **훅(Hooks)** – 사용자 입력 시점에 스크립트를 실행해 에이전트 동작 바꾸기
3. **MCP 서버** – 외부 프로그램(Blender)을 에이전트의 도구로 연결
4. **결과물 생성** – 에이전트로 이미지 생성 스크립트 작성 및 실행

## 실행 방법

카드뉴스 표지 생성:

```bash
pip install pillow
python make_cover.py
```

> Windows 기본 폰트(맑은 고딕)를 사용합니다. 다른 OS에서는 `FONT_BOLD`, `FONT_REGULAR` 경로를 바꿔 주세요.
