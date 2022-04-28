![TikTok RSS标志](https://tiktokrss.conoroneill.com/favicon-32x32.png)
# TikTok RSS使用GitHub OCTO扁平数据
* 使用[GitHub OCTO Flat Data](https://octo.github.com/projects/flat-data)、GitHub Actions 和 GitHub Pages 从 TikTok 生成可用的 RSS 源。

* 这使用非官方的[TikTokApi Python库](https://github.com/davidteather/TikTok-Api)从TikTok提取用户视频信息作为JSON，并为你感兴趣的每个用户生成RSS feeds。

* 要获得你自己的运行实例
    * 叉开这个 repo 
    * 为你的新 repo 启用 GitHub Pages
    * 将postprocessing.py中的`ghPagesURL`从 "https://conoro.github.io/tiktok-rss-flat/"改为你的网址
    * 将你喜欢的TikTok用户名添加到subscriptions.csv中。
    * 确保在Actions标签中启用Actions 

* 它被设置为每小时运行一次，在rss输出目录中为每个用户生成一个RSS XML文件。

* 然后你在[Feedly](https://www.feedly.com)或其他使用GitHub页面URL的feed阅读器中订阅每个feed。这些URL的构造是这样的。例如：。

    * TikTok 用户 = iamtabithabrown
    * XML文件 = rss/iamtabithabrown.xml
    * Feedly订阅URL = https://conoro.github.io/tiktok-rss-flat/rss/iamtabithabrown.xml
    * （或者在我的案例中，我为GitHub Pages项目设置了一个自定义域名，名为tiktokrss.conoroneill.com，该URL为https://tiktokrss.conoroneill.com/rss/iamtabithabrown.xml）
