const {chromium} = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: true,
    executablePath: 'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe'
  });
  
  const context = await browser.newContext();
  const page = await context.newPage();
  
  // 访问V2EX登录页
  await page.goto('https://www.v2ex.com/signin', { waitUntil: 'domcontentloaded', timeout: 30000 });
  console.log('V2EX登录页标题:', await page.title());
  
  // 查找登录表单
  const usernameInput = await page.locator('input[name="username"]').first();
  const passwordInput = await page.locator('input[name="password"]').first();
  
  if (await usernameInput.isVisible()) {
    console.log('✅ 找到登录表单');
    
    // 这里需要主人提供账号密码，或者使用cookie
    // 由于安全原因，建议手动登录后导出cookie
    console.log('⚠️ 需要手动登录或提供cookie');
    
  } else {
    console.log('❌ 未找到登录表单');
  }
  
  await browser.close();
})();
