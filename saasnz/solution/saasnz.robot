*** Settings ***
Documentation    Suite description
Library           SeleniumLibrary
Library           Collections
Library           BuiltIn
Library           ${keyword_library_path}/custom.py


*** Variables ***
${URL}    http://test.nz.agrisaas.com.cn/intelligent-agriculture/1.0.0/index/#/login
${Browser}    Chrome
${Username}    17300000000
${Password}    000000



*** Test Cases ***
登录
    open browser    ${URL}    ${Browser}
    Set Browser Implicit Wait    10
    Maximize Browser Window
    input text    xpath=//*[@id="app"]/div[1]/div/div/div[3]/form/div[1]/div/div/div/div/input    ${Username}
    input text    xpath=//*[@id="app"]/div[1]/div/div/div[3]/form/div[2]/div/div/div/div/input    ${Password}
    Click Element    xpath=/html/body/div[1]/div[1]/div/div/div[3]/div[1]/button
    Click Element    xpath=//*[@id="app"]/div[1]/div/div/div[7]/div/div[2]/div[2]/button/span
    Element Should Be Visible    xpath=//*[@id="app"]/div[1]/div[1]/div/div[1]


添加商品
     Add Product    苄嘧磺隆
     #搜索商品
     input text    xpath=//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div[1]/div/input    苄嘧磺隆
     click element    xpath=//*[@id="app"]/div[2]/div/div[2]/div[2]/div/div[2]/button/span
     #验证商品是否存在
     Element Should Be Visible    xpath=//*[@id="app"]/div[2]/div/div[3]/div[2]/table/tr/td[4]/div
     click element    xpath=//*[@id="app"]/div[2]/div/div[3]/div[2]/table/tr/td[12]/button[3]/span
     click element    xpath=/html/body/div[3]/div/div[3]/button[2]/span

入库登记
     Product Storage


销售出库
     Sale


获取库存数据
     Get Inventory


关闭浏览器
     close browser