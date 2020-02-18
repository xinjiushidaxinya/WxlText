<template>
<div>
<el-row>
<el-col :span="4">
      <div class="title">
      <span>租房网站后台管理系统</span></div>
      </el-col>
 <el-col :span="20" class="title-user" >
        <i class="el-icon-user"></i>
        <span>头像</span>
        <span>管理员</span>
</el-col>
</el-row>
<el-row>
  <el-col>
  <el-tabs :tab-position=" tabPosition" style="height:500px ;">
    <el-tab-pane label="租客网站的当前房源信息">
      <el-row>
        <el-col :span="4" v-for="(o, index) in 20" :key="o" :offset=1>
          <el-card :body-style="{ padding: '0px' }">
            <img src="../assets/fang3.jpg" class="image">
            <div style="padding: 14px;">
              <span>双人间</span>
              <div class="bottom clearfix">
                <el-button type="text" class="button">查看详情</el-button>
              </div>
            </div>
          </el-card>
          <div style="height: 10px;"></div>
        </el-col>
      </el-row>

     </el-tab-pane>
    <el-tab-pane label="用户管理">
      <el-table
         :data="tableData"
         style="width: 100%"
         max-height="250">
         <el-table-column
           fixed
           prop="leixing"
           label="房主信息"
           width="150">
         </el-table-column>
         <el-table-column
           prop="weizhi"
           label="租客信息"
           width="300">
         </el-table-column>

         <el-table-column
           fixed="right"
           label="操作"
           width="120">
           <template slot-scope="scope">
             <el-button
               @click.native.prevent="deleteRow(scope.$index, tableData)"
               type="text"
               size="small">
               预定
             </el-button>
           </template>
         </el-table-column>
       </el-table>
    </el-tab-pane>
    <el-tab-pane label="房源管理">
      <el-table
         :data="tableData"
         style="width: 100%"
         max-height="250">
         <el-table-column
           fixed
           prop="leixing"
           label="房源类型"
           width="150">
         </el-table-column>
         <el-table-column
           prop="weizhi"
           label="房源位置"
           width="300">
         </el-table-column>
         <el-table-column
           prop="province"
           label="房源价格"
           width="120">
         </el-table-column>
         <el-table-column
           prop="name"
           label="房主姓名"
           width="120">
         </el-table-column>
         <el-table-column
           prop="number"
           label="房主电话"
           width="120">
         </el-table-column>
         <el-table-column
           fixed="right"
           label="操作"
           width="120">
           <template slot-scope="scope">
             <el-button
               @click.native.prevent="deleteRow(scope.$index, tableData)"
               type="text"
               size="small">
               预定
             </el-button>
           </template>
         </el-table-column>
       </el-table>


    </el-tab-pane>
    <el-tab-pane label="订单管理">
      <el-table
         :data="tableData.filter(data => !search || data.name.toLowerCase().includes(search.toLowerCase()))"
         style="width: 100%">
         <el-table-column
           label="Date"
           prop="date">
         </el-table-column>
         <el-table-column
           label="Name"
           prop="name">
         </el-table-column>
         <el-table-column
           align="right">
           <template slot="header" slot-scope="scope">
             <el-input
               v-model="search"
               size="mini"
               placeholder="输入关键字搜索"/>
           </template>
           <template slot-scope="scope">
             <el-button
               size="mini"
               @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
             <el-button
               size="mini"
               type="danger"
               @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
           </template>
         </el-table-column>
       </el-table>
    </el-tab-pane>

    <el-tab-pane label="个人设置">
     </el-tab-pane>
  </el-tabs>
  </el-col>
</el-row>
</div>
</template>

<script>
  export default {
    data() {
      return {
          tabPosition: 'left',
          tableData: [{
                    date: '2016-05-02',
                    name: '王小虎',
                    address: '上海市普陀区金沙江路 1518 弄'
                  },
                  {
                            date: '2016-05-02',
                            name: '王小虎',
                            address: '上海市普陀区金沙江路 1518 弄'
                          }
                  ]
      };
    }
  }
</script>
<style>
  .title {
    height: 57px;
    line-height: 57px;
    background: #ffffff;
    font-size:18px;
    font-family:FZZYJW--GB1-0;
    color:rgba(89,187,255,1);
  }
  .title-user {
    background:#99A9BF;
    text-align: right;
    height: 57px;
    line-height: 57px;
    position: absolute;
    color: #FFFFFF;
    right: 15px;
    top: 0;
  }
  .title-user span {
    background:#99A9BF;
    height: 57px;
    line-height: 57px;
    margin-left: 15px;
  }
  .time {
      font-size: 13px;
      color: #999;
    }

    .bottom {
      margin-top: 13px;
      line-height: 12px;
    }

    .button {
      padding: 0;
      float: right;
    }

    .image {
      width: 100%;
      display: block;
    }

    .clearfix:before,
    .clearfix:after {
        display: table;
        content: "";
    }

    .clearfix:after {
        clear: both
    }
</style>
