CSS选择器

| 选择器             | 例子               | 例子描述                                                     |
| ------------------ | ------------------ | ------------------------------------------------------------ |
| .class             | .intro             | 选择class='intro'的所有节点                                  |
| #id                | #firstname         | 选择id='#firstname'的所有节点                                |
| *                  | *                  | 选择所有节点                                                 |
| element            | p                  | 选择所有\<p>标签=节点                                        |
| element，element   | div,p              | 选择所有\<div>节点和所有\<p>节点                             |
| element  element   | div  p             | 选择div内部的所有p节点                                       |
| element>element    | div>p              | 选择所有父节点为div的p节点                                   |
| element+element    | div+p              | 选择所有紧接在div节点之后的p节点                             |
| [attribute]        | [target]           | 选择所有带有target属性的节点                                 |
| [attribute=value]  | [target=block]     | 选择所有target=‘block’的节点                                 |
| [attribute~=value] | [title~=flower]    | 选择title属性包含flower单词的所有节点                        |
| :link              | a:link             | 选择所有违背访问的链接                                       |
| :visited           | a:visited          | 选择所有已被访问的链接                                       |
| :active            | a:active           | 选择活动链接                                                 |
| :hover             | a:hover            | 选择鼠标指针位于其上的连接                                   |
| :focus             | input:focus        | 选择获得焦点的input节点                                      |
| :first-letter      | p:fitst-letter     | 选择每个p节点的首字母                                        |
| :first-line        | p:first-line       | 选择每个p节点的首行                                          |
| :first-child       | p:first-child      | 选择属于父节点的第一个子节点的所有p节点                      |
| :before            | p:before           | 在每个p节点的内容之前插入内容                                |
| :after             | p:after            | 在每个p节点的内容之后插入内容                                |
| :lang(language)    | p:lang             | 选择所有it开头的lang属性值的所有p节点                        |
| element~enement    | p~ul               | 选择前面有p节点的所有ul节点                                  |
| [attribute^=value] | a[src^='https']    | 选择src属性值以https开头的所有a节点                          |
| [attribute$=value] | a[src$='.paf']     | 选择src属性值以.pdf结尾的所有a节点                           |
| [attribute*=value] | a[src*='abc']      | 选择src属性值中包含abc子串的a节点                            |
| :first-of-type     | p:first-of-type    | 选择属于父节点的首个p节点的所有p节点                         |
| :last-of-type      | p:last-of-type     | 选择属于父节点的最后p节点的所有p节点                         |
| :only-of-type      | p:only-of-type     | 选择属于父节点的唯一p节点的所有p节点                         |
| :only-child        | p:only-child       | 选择属于父节点的唯一子节点的所有p节点                        |
| :nth-child(n)      | p:nth-child        | 选择属于父节点的第二个子节点的所有p节点<br />（默认为第二个可以传入参数）<br />（p:nth-child(2n)，表示选取偶数位节点） |
| :nth-last-child(n) | p:nth-last-child   | 倒序，功能同上，从最后一个节点开始计数                       |
| :nth-of-type       | p:nth-of-type      | 选择属于父节点的第二个p节点的所有p节点<br />（默认为第二个，可以传入参数） |
| :nth-last-of-type  | p:nth-last-of-type | 同上，但是倒序                                               |
| :last-child        | p:last-child       | 选择属于父节点的最后一个子节点的所有p节点<br />（最后一子个节点不为p则不选中） |
| :root              | :root              | 选择文档根节点                                               |
| :empty             | p:empty            | 选择所有没有子节点的p节点<br />（包括文本子节点也不能有）    |
| :target            | #new:target        | 选择当前活动的#new节点                                       |
| :enable            | input:enable       | 选择每个启用的input节点                                      |
| :disable           | input:disable      | 选择每个禁用的input节点                                      |
| :checked           | input:checked      | 选择每个被选择的input节点                                    |
| :not(selector)     | :not(p)            | 选择非p节点的所有节点                                        |
| ::selection        | ::selection        | 选择被用户选取的节点部分                                     |

