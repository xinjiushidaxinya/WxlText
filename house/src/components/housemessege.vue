<template>
  <el-table :data="fangyuan" style="width: 100%" max-height="250">
    <el-table-column fixed prop="leixing" label="房源类型" width="150">
    </el-table-column>
    <el-table-column prop="weizhi" label="房源位置" width="300">
    </el-table-column>
    <el-table-column prop="province" label="房源价格" width="100">
    </el-table-column>
    <el-table-column prop="name" label="房主姓名" width="100">
    </el-table-column>
    <el-table-column prop="number" label="房主电话" width="100">
    </el-table-column>
    <el-table-column fixed="right" label="操作" align="center">
      <template slot="header" slot-scope="scope">
        <el-input v-model="search" size="mini" placeholder="输入关键字搜索" style="width: 180px;"/>
        <el-button size="small" style="width: 60px;">查找</el-button>
      </template>
      <template slot-scope="scope">
        <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
        <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
      </template>
    </el-table-column>
  </el-table>
</template>

<script>
</script>

<style>
</style>
