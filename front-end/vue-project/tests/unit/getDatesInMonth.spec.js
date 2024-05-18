import { expect } from 'chai';
import getDatesInMonth from '@/utils/getDatesInMonth';

describe('Calender.vue 使用的函式:', () => {
  it('找出當月開放日期(今天到兩週、避開星期日:true、其他:false)', () => {
    const result = getDatesInMonth(2024, 5); 
    const expected = [
      { "date": "05-01-2024", "open": false },
      { "date": "05-02-2024", "open": false },
      { "date": "05-03-2024", "open": false },
      { "date": "05-04-2024", "open": false },
      { "date": "05-05-2024", "open": false },
      { "date": "05-06-2024", "open": false },
      { "date": "05-07-2024", "open": false },
      { "date": "05-08-2024", "open": false },
      { "date": "05-09-2024", "open": false },
      { "date": "05-10-2024", "open": false },
      { "date": "05-11-2024", "open": false },
      { "date": "05-12-2024", "open": false },
      { "date": "05-13-2024", "open": false },
      { "date": "05-14-2024", "open": false },
      { "date": "05-15-2024", "open": false },
      { "date": "05-16-2024", "open": false },
      { "date": "05-17-2024", "open": false },
      { "date": "05-18-2024", "open": true },
      { "date": "05-19-2024", "open": false },
      { "date": "05-20-2024", "open": true },
      { "date": "05-21-2024", "open": true },
      { "date": "05-22-2024", "open": true },
      { "date": "05-23-2024", "open": true },
      { "date": "05-24-2024", "open": true },
      { "date": "05-25-2024", "open": true },
      { "date": "05-26-2024", "open": false },
      { "date": "05-27-2024", "open": true },
      { "date": "05-28-2024", "open": true },
      { "date": "05-29-2024", "open": true },
      { "date": "05-30-2024", "open": true },
      { "date": "05-31-2024", "open": true }
    ];

    expect(result).to.deep.equal(expected);
  });
});
