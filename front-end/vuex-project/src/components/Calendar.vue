<template>
  <div class="weekdays">
    <div class="weekday" v-for="day in weekdays" :key="day">{{ day }}</div>
  </div>
  <div class="days">
    <div class="blank" v-for="blank in firstDayOfWeek"></div>
    
    <template v-for="(data,index) in datesArray"  >
      <div class="blank-circle" v-if="data.open" :key="'day' + index">
        
        <div class="circle-container">
          <TheCircleProgress :day="index+1"/>
        </div>
      </div>
      <div class="day" v-else :key="'blank-circle' + index">
       <div class="circle-container">
          <TheCircleBlank :day="index+1"/>
        </div>
      </div>
    </template>
   
  </div>
</template>

<script>
import TheCircleProgress from "../components/TheCircleProgress.vue";
import TheCircleBlank from "../components/TheCircleBlank.vue";
import { ref, computed } from "vue";
export default {
  components: {
    TheCircleProgress,
    TheCircleBlank,
  },
  setup() {
    const weekdays = ref(["日", "一", "二", "三", "四", "五", "六"]);

    // 計算當月第一天是星期幾
    const firstDayOfWeek = computed(() => {
      return new Date(2024, 3, 1).getDay();
    });

    // 找出當月所有開放日期、開放設置為true，組成陣列，並跳過星期日
    const getDatesInMonth = (year, month) => {
      const today = new Date();
      const twoWeeksLater = new Date(
        today.getTime() + 13 * 24 * 60 * 60 * 1000
      );
      const startDate = new Date(year, month - 1, 1);
      const endDate = new Date(year, month, 0);
      const datesArray = [];

      for (
        let date = new Date(startDate);
        date <= endDate;
        date.setDate(date.getDate() + 1)
      ) {
        console.log("date", date);
        console.log("startDate", startDate);

        // if (date.getDay() === 0) continue;

        const formattedDate = date
          .toLocaleDateString("en-US", {
            year: "numeric",
            month: "2-digit",
            day: "2-digit",
          })
          .replace(/\//g, "-");

        date.setHours(0, 0, 0, 0);
        today.setHours(0, 0, 0, 0);
        twoWeeksLater.setHours(0, 0, 0, 0);

        const isOpen = date >= today && date <= twoWeeksLater;

        datesArray.push({ date: formattedDate, open: isOpen });
      }

      return datesArray;
    };

    const datesArray = getDatesInMonth(2024, 4);
    console.log(datesArray);

    return {
      weekdays,
      firstDayOfWeek,
      datesArray,
    };
  },
};
</script>

<style lang="scss" scoped>
.weekdays {
  display: flex;
  justify-content: space-between;
  margin-top: 40px;
  .weekday {
    text-align: center;
    width: calc(100% / 7);
  }
}

.days {
  margin-top: 40px;
  display: grid;
  text-align: center;
  grid-template-columns: repeat(7, 1fr);
  .blank,
  .blank-circle,
  .day {
    margin-top: 20px;
  }
  .circle-container {
    display: flex;
    justify-content: center;
  }
}
</style>
