// UserPromptSubmit 훅: 프롬프트에 "뿅"이 포함되면 추가 지시문을 컨텍스트에 주입
let input = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (chunk) => (input += chunk));
process.stdin.on('end', () => {
  let prompt = '';
  try {
    prompt = JSON.parse(input).prompt || '';
  } catch (e) {
    process.exit(0);
  }

  if (!prompt.includes('뿅')) process.exit(0);

  const now = new Date().toLocaleString('ko-KR', { timeZone: 'Asia/Seoul' });
  const message = `사용자의 요청에 정상적으로 답변하면서 응답의 마지막에는 "빵빵 ${now}"을 같이 붙여서 답변하세요.`;

  process.stdout.write(
    JSON.stringify({
      hookSpecificOutput: {
        hookEventName: 'UserPromptSubmit',
        additionalContext: message,
      },
    })
  );
});
