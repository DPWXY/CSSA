// pages/lottery_results/lottery_results.js
const app = getApp()
const classesId = "8f9ff639611a410d00aaa7ba5e2491d6"
const db = wx.cloud.database()
const lotteryCollection = db.collection("lottery")
const _ = db.command

Page({

  /**
   * 页面的初始数据
   */
  data: {
    second_price_number: 4,
    user_id1: [{
      image1: "/images/cssa-logo.jpg",
      userText1: "small shrimp111"
    }],
    user_id2: [{
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
    {
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp2"
    },
    ],
    user_id3: [{
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
    {
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp2"
    },
    {
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
    {
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
    {
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
    ],
    user_id0: [{
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
    {
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
    {
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
    {
      image: "/images/cssa-logo.jpg",
      userText: "small shrimp1"
    },
]
  },

  GUP: function(event){
    const app = getApp()
    const db = wx.cloud.database()
    const lotteryCollection = db.collection("lottery")
    const _ = db.command
    const info = lotteryCollection.doc("6f49505e6264a36101efbb9d27e19df3").get({
      success: function(res) {
        // res.data 包含该记录的数据
        const data = res.data
        const first_n = res.data.first.nickName
        console.log(data)
        this.setData({
          'user_id1.image1': res.data.first.avatarUrl,
          'user_id1.userText1': first_n,
          data_first: res.data.first,
          data_second: res.data.second,
          data_third: res.data.third,
          data_luck: res.data.luck
        })
      }
    })
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {

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