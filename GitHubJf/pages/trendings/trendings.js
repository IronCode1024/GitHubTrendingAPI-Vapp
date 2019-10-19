// pages/trendings/trendings.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    githubData:[{about:"",
    avatars: (5) [""],
    forks: "2,263",
    language: "",
    link: "https://github.com/openwrt/openwrt",
    new_stars: "10 stars today",
    repo: "openwrt",
    stars: "3,705",
    user: "openwrt"}],
    title:"标题（账户名称/项目库名称）",
    explain:"说明预览",
    languagetab:"语言",
    ImgUrl:"/images/backimg/mao.jpg",
    datagit:[]  
  },

  /**
   * 生命周期函数--监听页面加载
   */
  //http://anly.leanapp.cn/api/github/trending/java?since=weekly
  onLoad: function (options) {
    var that = this;
    wx.request({
      url: 'https://api.github.com/users/ironman1024/repos',
      header: {
        'Content-Type': 'application/json'
      },
      success: function(res) {
        console.info(res.data.msg[0])
        var datagit=res.data.msg;
        var element="";
        for (let index = 0; index < datagit.length; index++) {
          var repo='githubData['+index+'].repo';
          var abouts='githubData['+index+'].about';
          var stars='githubData['+index+'].stars';
          var forks='githubData['+index+'].forks';
          var link='githubData['+index+'].link';
          var user='githubData['+index+'].user';
          var language='githubData['+index+'].language';
          element = datagit[index].about;
          if (element.length > 17) {
           var s = element.substring(0, 50) + "...";
           that.setData({
            [abouts]:s,
            [repo]:datagit[index].repo,
            [stars]:datagit[index].stars,
            [forks]:datagit[index].forks,
            [link]:datagit[index].link,
            [user]:datagit[index].user,
            [language]:datagit[index].language
          });
          }
        }
        
        // that.setData({
        //   githubData:res.data.msg
        // });
      }
    })
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {

  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {

  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {

  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {

  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {

  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {

  }
})