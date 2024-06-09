// 找出當月所有開放日期、開放設置為true，組成陣列，並跳過星期日
function getDatesInMonth(year, month) {
  const today = new Date();
  const twoWeeksLater = new Date(today.getTime() + 13 * 24 * 60 * 60 * 1000);
  const startDate = new Date(year, month - 1, 1);
  const endDate = new Date(year, month, 0);
  const datesArray = [];

  for (
    let date = new Date(startDate);
    date <= endDate;
    date.setDate(date.getDate() + 1)
  ) {
    // console.log("date", date); 
    // console.log("startDate", startDate);

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

    const isOpen =
      date >= today && date <= twoWeeksLater && date.getDay() !== 0;

    datesArray.push({ date: formattedDate, open: isOpen });
  }

  return datesArray;
}

export default getDatesInMonth;
