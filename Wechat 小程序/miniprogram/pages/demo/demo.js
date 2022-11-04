// pages/demo/demo.js
Page({

    /**
     * 页面的初始数据
     */
    data: {
        // demo
        x: 123455,
        y: 5543321,
        k: 55555,
        // demo 循环
        l: [2,3,4,5,6],
        b: true,
        c: false
    },

    /**
     * 生命周期函数--监听页面加载
     */
    onLoad: function (options) {
        // demo 1
        var x = 3;
        // let x = 3; /*局部变量*/
        // const x = 3; /*无法改变*/
        console.log(x);
        // demo 2 在此设置也可以输出z 把后端数据显示在页面上
        this.setData({
            z: 789
        })
    },
    // demo3
    onTap: function (event) {
        //demo 1
        // console.log("tapping")

        // demo 2 when tap, change number
        // this.setData({
        //     x: 78889
        // })

        // demo 3 用里面的值 然后每点一次加一
        // console.log(this.data.x)
        // this.setData({
        //     x: this.data.x + 1
        // })

        // demo 4 点击之后变成想设置的值 从前端把值带入后端
        this.setData({
            k: event.currentTarget.dataset.demo
        })
    },
    
    onTap2: function (event){
        wx.navigateTo({
          url: '/pages/demo2/demo2?ok=666&ok2=333',
        })

        // other 页面切换
        // wx.switchTab({
        //   url: 'url',
        // })
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