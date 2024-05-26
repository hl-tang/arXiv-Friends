API文档: http://127.0.0.1:8000/api/docs





PaperRow作为子组件被Home和SearchResult引用，Home和SearchResult通过axios从后端获得数据，通过props传给PaperRow

在PaperRow.vue里

```ts
const props = defineProps({
  paper_id: String,
  title_en: String,
  title_ja: String,
  authors: Array,
  published: String,
  content_en: String,
  pdf_url: String,
  categories: Array
})
const { paper_id, title_en, title_ja, authors, published, content_en, pdf_url, categories } = toRefs(props);
```



状态管理 + 持久化localStorage





### 收藏

home或searchresult因为不知道用户到底收藏了没有，前端先统一显示灰色的星星(`const isLiked = ref(false);`)。点击收藏按钮后，post访问/like/这个接口。

然后后端判断是否已经收藏过了(userlikepaper表里有没有这条记录)，是的话就返回msg说已经收藏了，然后前端把星星变黄。如果确实没收藏过，那就数据库里加一条记录，然后前端把星星变黄。

取消收藏：前端对着一个黄色星星点击后，delete方法访问/like/接口，把数据库记录删掉。星星变灰。

用户mypage前端统一显示黄色的星星(`const isLiked = ref(true);`)，因为都是肯定已经收藏了的。



### 关于emit

然后碰到的一个问题就是，我在子组件PaperRow点击了收藏按钮想要取消收藏，之后怎么触发某个写在MyPage.vue里的handleClickFavorites函数用以重新获取likedPapers(取消收藏的删掉)和收藏数统计来重新渲染呢？

子组件里defineEmits定义事件,子组件PaperRow `axios.delete('/api/like/)`后`emit('cancel-like-at-my-page');`来通知父组件。父组件MyPAge.vue里`<PaperRow @cancel-like-at-my-page="renewFavorites" />`收到emit便会触发renewFavorites函数,访问后端`axios.get('/api/like/')`重新渲染页面.

**但子组件emit记得写在axios.then里面** *保证后端数据库写入返回了再hit get endpoint*

起初我还在父组件MyPage的触发函数里setTimeout设置0.5s延迟访问，想到PaperRow那里delete请求数据库还没做完，导致这里显示有问题(*可能数据库还没写入，就去访问api了，而这时的返回结果就不对了因为数据库还没更新*)。

后来发现是emit写在了axios的外面，导致异步先去get访问api了。就和loading的问题一样。



