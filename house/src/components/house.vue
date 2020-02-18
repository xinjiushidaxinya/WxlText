<template>
  <div>
    <Layout>
      <Header>
        <el-row span="24" class="daohanglan">
          <el-col :span="22">
            <i class="el-icon-s-home" style="margin-right: 10px"></i>
            <span class="dingbu">租家网站</span></el-col>
          <el-col :span="2">
            <div style="margin-top: 10px;">
              <el-button type="text" class="anniu" @click="denglu">首页</el-button>
            </div>
          </el-col>
          <el-col span="24">
            <el-carousel :interval="4000" type="card" height="200px">
              <el-carousel-item v-for="item in imglist" :key="item.id">
                <img v-bind:src="item.idView" class="imgs" />
              </el-carousel-item>
            </el-carousel>
          </el-col>
        </el-row>
      </Header>
      <Content>
        <el-table :data="tableData" style="width: 100%" max-height="250">
          <el-table-column fixed prop="leixing" label="房源类型" width="150">
          </el-table-column>
          <el-table-column prop="weizhi" label="房源位置" width="300">
          </el-table-column>
          <el-table-column prop="province" label="房源价格" width="120">
          </el-table-column>
          <el-table-column prop="name" label="房主姓名" width="120">
          </el-table-column>
          <el-table-column prop="number" label="房主电话" width="120">
          </el-table-column>
          <el-table-column fixed="right" label="操作" width="120">
            <template slot-scope="scope">
              <el-button @click.native.prevent="deleteRow(scope.$index, tableData)" type="text" size="small">
                预定
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </Content>
    </Layout>
  </div>
</template>

<script>
  /*eslint-disable*/
  export default {
    data() {
      return {
        imglist: [{
            id: 0,
            idView: require('../assets/fang1-1.jpg')
          },
          {
            id: 1,
            idView: require('../assets/fang2-1.jpg')
          },
          {
            id: 2,
            idView: require('../assets/fang3-1.jpg')
          },
          {
            id: 3,
            idView: require('../assets/fang4.jpg')
          },
          {
            id: 4,
            idView: require('../assets/fang5.jpg')
          },
          {
            id: 5,
            idView: require('../assets/fang7.jpg')
          }
        ],
        tableData: [{
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          }, {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          },
          {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          },
          {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          },
          {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          },
          {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          },
          {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          },
          {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          },
          {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          },
          {
            leixing: '双人间',
            weizhi: '上海市普陀区金沙江路 1518 弄',
            province: '900/月',
            name: '武鑫林',
            number: '88888888'
          }
        ]
      }
    },
    methods: {
      denglu() {
        this.$router.push({
          path: './login'
        })
      }
    }
  }
</script>

<style>
  .el-icon-s-home {
    color: #FFFFFF;
  }

  .dingbu {
    color: rgba(89, 187, 255, 1);
    line-height: 60px;
    font-family: FZZYJW--GB1-0;
    font-size: 20px;
    text-shadow: 0.1em 0.1em 0.15em #1E90FF;
  }

  .daohanglan {
    background-color: #99A9BF;
    height: 60px;
  }

  .anniu {
    color: #FFFFFF;
  }

  .imgs {
    height: 100%;
    width: 100%;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
</style>
