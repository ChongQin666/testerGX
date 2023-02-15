<template>
<div class="box">
    <div>
      <el-input v-model="input" placeholder="请输入测试员工号" style="width:300px"></el-input>
      <el-button type="success" @click="addUser">添加</el-button>
    </div>
    <el-table
      :data="tableData"
      style="width: 600px;">
      <el-table-column
        prop="fields.user_name"
        label="测试员工号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="fields.add_time"
        label="添加时间">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: "UserTest",
  data () {
    return {
      input: '',
      tableData: []
    }
  },
  created () {
    this.showUser()
  },
  methods: {
    showUser () {
      this.axios.get('show_users/')
        .then((response) => {
            console.log(response.data.list);
            this.tableData = response.data.list
        })
        .catch(function (error) {
            console.log(error);
        });
    },
    addUser () {
      this.axios.get('add_user/',{params:{user_name: this.input}})
        .then((response) => {
            console.log(response.data.msg);
            this.showUser()
        })
        .catch(function (error) {
            console.log(error);
        });
    }
  }
}
</script>

<style scoped>
.box{
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: center;
}
</style>
