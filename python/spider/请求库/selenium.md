selenium

基本使用

> ```python
> from selenium import webdriver
> from selenium.webdirver.common.by import By
> from selenium.webdirver.common.keys import Keys
> from selenium.webdirver.support import expected_conditions as EC
> from selenium.webdirver.support.wait import WebDriverWait
> 
> # 声明浏览器对象
> brower = webdriver.Chrome()
> try:
>     # 请求页面
>     brower.get('http://baidu.com')
>     # 获取节点
>     input = brower.find_element_by_id('kw')
>     # 节点操作，在输入框输入python
>     input.send_keys('python')
>     # 节点操作，模拟按键enter
>     input.send_key(Keys.ENTER)
>     # 设置浏览器等待时长
>     wait = WebDriverWait(brower, 10)
>     # 显示等待元素出现
>     wait.until(EC.presence_of_element_located((By.ID,'content_left')))
>     # 获取当前url
>     print(brower.current_url)
>     # 获取当前cookie
>     print(brower.get_cookies)
>     # 获取当前页面源代码
>     print(brower.page_source)
>     brower.close()
> except:
>     print('Error')
>     brower.close()
> ```
>
> 

声明浏览器

> selenium支持大多主流浏览器，需要下载浏览器官方的自动化程序放到python的script文件夹中才能被调用
>
> ```python
> webdriver.Chrome()
> webdriver.Firefox()
> webdriver.Edge()
> webdriver.PhantomJS()
> webdriver.Safari()
> ```
>
> 

访问页面

> ```python
> browser = webdriver.Chrome()
> # 浏览器对象的get方法用于请求页面，不会携带cookie
> browser.get(url)
> ```

查找节点

> ```python
> # 单个节点查找方法
> find_element_by_id()
> find_element_by_name()
> find_element_by_xpath()
> find_element_by_link_text()
> find_element_by_tag_name()
> find_element_by_class_name()
> find_element_by_css_selector()
> # 或者以By的方式选择查找节点的方式find_element(By.ID,'q')
> 
> # 多个节点查找方法
> find_elements_by_id()
> find_elements_by_name()
> find_elements_by_xpath()
> find_elements_by_link_text()
> find_elements_by_tag_name()
> find_elements_by_class_name()
> find_elements_by_css_selector()
> # 或者以By的方式选择查找节点的方式find_elements(By.ID,'q')
> ```
>
> 

节点交互

> ```python
> #常见的节点交互动作
> # 在节点中输入，常用于输入框
> send_keys()
> # 清空节点中的输入，崔永元输入框
> clear()
> # 节点单击动作，常用于按钮
> click()
> # 更多动作，查找官方文档
> ```
>
> 

动作链

> ```python
> # 网页中的一些交互是没有特点节点，比如鼠标拖拽，在页面任意处按下按键
> # 这些动作的执行就需要通过动作链取执行
> 
> from selenium import webdriver
> from selenium.webdriver import ActionChains
> 
> browser = webdriver.Chrome()
> browser.get(url)
> source = browser.find_element_by_css_selector('#source')
> target = browser.find_element_by_css_selector('#target')
> # 传入浏览器对象创建动作连对象
> actions = ActionChains(broswer)
> # 创建拖拽动作
> actions.drag_and_drop(source, target)
> # 执行动作
> actions.perform()
> ```
>
> 

执行JavaScript

> ```python
> # webdriber实例使用execute_script()方法去使用JavaScript代码，以完成一些selenium中没有实现的功能
> broswer = webdriver.Chrome()
> broswer.get(url)
> broswer.execute_script('alert("hello")')
> ```
>
> 

获取节点信息

> ```python
> # 获取节点属性，get_attribute()，方法
> logo = browser.find_element((By.ID,'logo'))
> name = logo.get_attribute('name')
> 
> # 获取节点文本，text属性
> txt = logo.text
> 
> # 节点的一些其他属性，获取id、相对位置，标签名称、节点宽高
> logo.id
> logo.location
> logo.tag_name
> logo.size
> ```
>
> 

切换Frame

> ```python
> # 进入子页面，子页面的查找节点，交互节点都需要进入子页面之后才能正常操作
> browser.switch_to.frame('iframe')
> browser.find_element()
> # 返回父页面
> browser.switch_to_parent_frame()
> ```
>
> 

延迟等待

> 隐式等待：当没有DOM中找到节点时，将等待一段时间在查找节点
>
> ```python
> # 调用implicitly_wait()方法设置元素未发现时的等待时长
> broswer.implicitly_wait(10)
> broswer.get(url)
> # 元素未发现则，等待10s在进行查找
> broswer.find_element()
> ```
>
> 显示等待：设置一个最长时间，在这个时间内元素出现则结束等待，超出时间则抛出异常：元素没有发现
>
> ```python
> # 显示等待需要依赖这两个类，WebDriverWait设置等待时长，EC设置等待条件
> from selenium.webdirver.support import expected_conditions as EC
> from selenium.webdirver.support.wait import WebDriverWait
> 
> # 传入浏览器对象，设置最大等待时长
> wait = WebDriverWait(browser, 10)
> # 设置等待条件，当条件达成时则退出等待
> # EC.presence_of_element_located((By.ID, 'q'))表示等待ID=q的节点加载出来
> input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
> 
> # 常见的等待条件
> EC.presence_of_element_located() #节点出现
> EC.visibility_of_element_located() #节点可见
> EC.invisibility_of_element_located() #节点不可见
> EC.element_to_be_clickable() #节点可点击
> EC.element_located_to_be_selected() #节点可选择
> 
> #更多条件见P260或官方文档
> ```
>
> 

前进后退

> ```python
> # back()方法，表示后退
> broswer.back()
> # forward()方法，表示前进
> borswer.forward()
> ```
>
> 

选项卡操作（句柄操作）

> ```python
> # 当浏览器有多个页面时，想要操作某个页面就需要进入该页面才能进行节点操作
> # 要进入某个页面就需要该页面的句柄，也就是开始地址
> # browser.window_handles属性中保存着浏览器所有选项卡的句柄，保存形式为列表
> pages = browser.window_handles
> # 浏览器越新打开的页面在列表中下标越大，switch_to_window()接受一个句柄，用于进入某个页面
> # 所以这里进入的就是最新打开的页面
> broswer.switch_to_window(pages[-1])
> ```
>
> 

异常捕获

> ```python
> # selenium.common.exceptions中定义了selenium使用过程中常见的异常类型
> # 可以通过捕获这些异常进行下一步操作
> # 更多异常参考官方文档
> from selenium.common.exceptions import TimeoutException, NoSuchElementException
> 
> try:
>     pass
> except NoSuchElementException: # 捕获节点不存在异常
>     pass
> ```
>
> 