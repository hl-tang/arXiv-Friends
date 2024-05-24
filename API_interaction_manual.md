API文档: http://127.0.0.1:8000/api/docs







### 收藏

home或searchresult前端先统一显示灰色的星星(`const isLiked = ref(false);`)，不知道用户到底收藏了没有。点击收藏按钮后，post访问/like/这个接口。

然后后端判断是否已经收藏过了(userlikepaper表里有没有这条记录)，是的话就返回msg说已经收藏了，然后前端把星星变黄。如果确实没收藏过，那就数据库里加一条记录，然后前端把星星变黄。

取消收藏：前端对着一个黄色星星点击后，delete方法访问/like/接口，把数据库记录删掉。星星变灰。

用户mypage前端统一显示黄色的星星(`const isLiked = ref(true);`)
