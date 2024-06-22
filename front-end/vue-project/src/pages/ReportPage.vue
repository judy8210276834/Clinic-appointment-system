<script>
import BreadDoctor from "../components/BreadDoctor.vue";
export default {
  components: {
    BreadDoctor,
  },
};
</script>
<template>
  <BreadDoctor />
  <div class="report_page_board">
    <table>
      <tr>
        <th>2023</th>
        <th>預約總人數</th>
        <th>現場總人數</th>
        <th>取消總人數</th>
        <th>預約未到總人數</th>
        <th>繳費總人數</th>
        <th>總金額</th>
      </tr>
      <tr v-for="(item,idx) in 12">
        <td>{{ idx+1 }}月</td>
        <td>423432433</td>
        <td>2432424</td>
        <td>2342423</td>
        <td>324242</td>
        <td>23432424</td>
        <td>546646</td>
      </tr>
    </table>
  </div>
</template>

<style scoped lang="scss">
@import "@/assets/_variables.scss";

.report_page_board {
  background-color: white;
  // height: 690px;
  padding: 84px;

  font-weight: bold;
  color: $primaryMiddle;
  text-align: center;

  table {
    width: 100%;
    font-size: 20px;
    th {
      background-color: #c2bfaf;
      padding: 8px;
    }
    td {
      padding: 8px;
      background-color: rgba(194, 191, 175, 0.6);
    }
  }

  @media screen and (max-width: $medium) {
    padding: 84px;
    height: 530px;
    font-size: 16px;
  }

  @media screen and (max-width: $small) {
    padding: 40px;
    height: 400px;
    font-size: 16px;
  }
}
</style>
