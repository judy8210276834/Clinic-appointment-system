<script>
import TheCircleProgress from "../components/TheCircleProgress.vue";
import BreadCrumbs from "../components/BreadCrumbs.vue";
import Calendar from "../components/Calendar.vue";
import { reactive,ref } from "vue";
export default {
  components: {
    TheCircleProgress,
    BreadCrumbs,
    Calendar
  },
  setup() {
    const breadcrumbs = reactive([
      {
        label: "預約日期",
        url: { name: "choose_date" },
      },
      {
        label: "預約時間",
        url: { name: "choose_time" },
      },
      {
        label: "報表",
      },
    ]);
    const currentDate = new Date();
    const year = ref(currentDate.getFullYear());
    const month = ref(currentDate.getMonth() + 1);

    const addMonth = () => {
      month.value++;
      if(month.value > 12){
        month.value = 1;
        year.value++;
      }
    };

    const minusMonth = () => {
      month.value--;
      if (month.value < 1) {
        month.value = 12;
        year.value--;
      }
    };
    return {
      breadcrumbs,
      year,
      month,
      addMonth,
      minusMonth
    };
  },
};
</script>

<template>
  <BreadCrumbs :items="breadcrumbs" />
  <!-- <TheCircleProgress /> -->
  <div class="board">
    <fa class="minusMonth" icon="caret-left" @click="minusMonth"/> <span>{{ year }}</span> ． <span>{{ month }}</span> <fa class="addMonth" icon="caret-right" @click="addMonth"/>
    <Calendar :year="year" :month="month"/>
  </div>
  

</template>


<style lang="scss" scoped>
@import '@/assets/_variables.scss'; 

.board{
  background-color: white;
  height: 690px;
  margin-top: 20px;
  padding: 84px 84px 0px 84px;
  font-size: 24px;
  font-weight: bold;
  color: #81766fa0;
  text-align: center;
  .minusMonth,.addMonth{
    cursor: pointer;
    font-size: 18px;
  }

  @media screen and (max-width: $medium) {
    padding: 84px 84px 0px 84px; 
    height: 530px; 
    font-size: 20px;
  }
  
  @media screen and (max-width: $small) {
    padding: 40px 40px 40px 40px; 
    height: 400px;  
    font-size: 20px;
  }
}
</style>
