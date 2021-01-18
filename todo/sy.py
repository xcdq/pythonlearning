import re
st = """<ul class="category_newlist">
                        <li><a href="forum.php?mod=viewthread&amp;tid=363028&amp;extra=" tip="标题: <strong>1.16更新【huiasd（灰灰）】作
品合集</strong><br/>作者: kxdlxm (<span title='2021-1-16'>8&nbsp;分钟前</span>)<br/>查看/回复: 26/1" onmouseover="showTip(this)" target="_blank">1.16更新【huiasd（灰灰）】作品 ...</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=363020&amp;extra=" tip="标题: <strong>四本长篇后宫文合贴，《我养了一只狐妖
女儿》《看守魔女们的典狱长》《吾妻非人哉》等</strong><br/>作者: 深拥女王钻石心 (<span title='2021-1-16'>半小时前</span>)<br/>查看/回复: 
613/77" onmouseover="showTip(this)" target="_blank">四本长篇后宫文合贴，《我养了一 ...</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=363018&amp;extra=" tip="标题: <strong>【重生笑傲江湖】第一篇 前传（01-29）
作者：qslq123 更新29</strong><br/>作者: cyl780709 (<span title='2021-1-16'>1&nbsp;小时前</span>)<br/>查看/回复: 322/43" onmouseover="showTip(this)" target="_blank">【重生笑傲江湖】第一篇 前传（0 ...</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=363016&amp;extra=" tip="标题: <strong>【重生笑傲江湖】第一篇 前传（01-28）
作者：qslq123 更新28</strong><br/>作者: cyl780709 (<span title='2021-1-16'>1&nbsp;小时前</span>)<br/>查看/回复: 127/12" onmouseover="showTip(this)" target="_blank">【重生笑傲江湖】第一篇 前传（0 ...</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=363007&amp;extra=" tip="标题: <strong>《无限取代》（珍藏1-17卷65章）作者：
天凰羽</strong><br/>作者: cyl780709 (<span title='2021-1-16'>2&nbsp;小时前</span>)<br/>查看/回复: 561/67" onmouseover="showTip(this)" target="_blank">《无限取代》（珍藏1-17卷65章） ...</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=363006&amp;extra=" tip="标题: <strong>豪乳老师刘艳（同人续作）豪乳教师少妇
刘艳之二卷】《少妇沉沦，美人劫波09》更新09</strong><br/>作者: cyl780709 (<span title='2021-1-16'>2&nbsp;小时前</span>)<br/>查看/回复: 383/68" onmouseover="showTip(this)" target="_blank">豪乳老师刘艳（同人续作）豪乳教 ...</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=362997&amp;extra=" tip="标题: <strong>最新更新母子血亲舅妈的不伦亲情第二部
（64）</strong><br/>作者: wb890920 (<span title='2021-1-16'>3&nbsp;小时前</span>)<br/>查看/回复: 1151/163" onmouseover="showTip(this)" target="_blank">最新更新母子血亲舅妈的不伦亲情 ...</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=362978&amp;extra=" tip="标题: <strong>喜欢就下！！！！</strong><br/>作者: 
冥月死神 (<span title='2021-1-16'>9&nbsp;小时前</span>)<br/>查看/回复: 4692/508" onmouseover="showTip(this)" target="_blank">喜欢就下！ 
！！！</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=362973&amp;extra=" tip="标题: <strong>喜欢下载！！！！</strong><br/>作者: 
冥月死神 (<span title='2021-1-16'>9&nbsp;小时前</span>)<br/>查看/回复: 3478/292" onmouseover="showTip(this)" target="_blank">喜欢下载！ 
！！！</a></li>
                <li><a href="forum.php?mod=viewthread&amp;tid=362969&amp;extra=" tip="标题: <strong>【诡秘归来(诡秘之主同人)】【1-4章加 
番外2篇】【作者：光焰百合】</strong><br/>作者: 39448 (<span title='2021-1-16'>10&nbsp;小时前</span>)<br/>查看/回复: 2302/731" onmouseover="showTip(this)" target="_blank">【诡秘归来(诡秘之主同人)】【1- ...</a></li>
         </ul>"""
root_pattern = '<ul class="category_newlist">.*?</ul>'
r = re.findall(root_pattern, st)
print(r)
