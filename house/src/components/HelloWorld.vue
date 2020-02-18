<template>
  <div class="home">
    <el-row class="tac">
      <!-- 导航菜单 -->
      <el-col :span="4" class="left">
        <el-row>
          <el-col :span="24"><div class="title"><span >租客网站后台管理系统</span></div></el-col>
        </el-row>
         <el-menu default-active="2" @open="handleOpen" @close="handleClose" @select="handleSelect" router unique-opened>
          <el-submenu :index="index.toString()" v-for="(item, index) in navData" :key="index">
            <template slot="title">
              <i :class="item.icon"></i>
              <span>{{ item.name }}</span>
            </template>
              <el-menu-item :index="even.path" v-for="(even, index) in item.evens" :key="index" style="color: rgba(89,187,255,1)">{{ even.name }}</el-menu-item>
          </el-submenu>
        </el-menu>
      </el-col>
      <!-- 右面内容 -->
      <el-col :span='20'>
        <el-row>
          <el-col :span="24">
            <div class="top">
              <el-breadcrumb separator=">">
                <el-breadcrumb-item v-for="(item, index) in bread" :to=item.path :key='index' style="color: #1E90FF;">{{item.name}}</el-breadcrumb-item>
              </el-breadcrumb>
              <span class="title-user">
                <i class="el-icon-user"></i>
                <span>头像</span>
                <span>管理员</span>
              </span>
            </div>
          </el-col>
          <el-col :span="24"><div class="body"><router-view></router-view></div></el-col>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
 export default {
    name: 'home',
    data() {
      return {
        navData: [
          { num: 1 , name: "房源管理", icon: 'el-icon-house' , evens: [ { name:'房源表',path: '/HelloWorld/housemessege' } ] },
          { num: 2 , name: "用户管理", icon: 'el-icon-s-custom' , evens: [ { name: '用户表', path: '/HelloWorld/housedata'}]},
          { num: 3 , name: "订单管理", icon: 'el-icon-tickets' , evens: [ { name:'订单表', path: '/HelloWorld/dingdan' }]},
          { num: 4 , name: "系统设置", icon: 'el-icon-setting' , evens: [ { name:'修改密码', path: '/HelloWorld/xiugai' } ] },
           ],
        bread : [],
      }
    },
    methods: {
      handleOpen(key, keyPath) {
        this.bread = [];
        this.bread.push(this.navData[key])
      },
      handleClose(key, keyPath) {
        // console.log(key, keyPath);
        this.bread = []
      },
      handleSelect(key, keyPath) {
        this.bread.length = 1;
        let date = this.navData[keyPath[0]].evens
        for (let key in date) {
          if(date[key].path == keyPath[1]){
            this.bread.push(date[key])
          }
        }
      }
    }
  }
</script>

<style scoped>
  .home {
    height: 100%;
  }
  .tac {
    height: 100%;
  }
  .left {
    height:100%;
    background: #ffffff;
  }
  .title {
    height: 57px;
    line-height: 57px;
    padding-left: 5%;
    background: #ffffff;
    font-size:18px;
    font-family:FZZYJW--GB1-0;
    font-weight:400;
    color:rgba(89,187,255,1);
  }
  .top {
    height:57px;
    line-height:57px;
    background:#99A9BF;
    text-align: right;
  }

  .body {
    margin-left: 12px;
    margin-right: 26px;
  }

  .el-breadcrumb {
    height: 57px;
    line-height: 57px;
    margin-left: 12px;
  }
  .title-user {
    position: absolute;
    color: #FFFFFF;
    right: 15px;
    top: 0;
  }
  .title-user span {
    margin-left: 15px;
  }
</style>
