import { expect } from 'chai';
import { validateForm } from '@/utils/validateCheck';

let errors;

before(() => {
  errors = { name: '', email: '', password: '' };
});

describe('確認註冊資料都有填寫:', () => {
  // type = true代表登入
  it('資料都填了', () => {
    const userData = { name: 'John Doe', email: 'john.doe@example.com', password: '123456' };
    const isValid = validateForm(false, userData, errors); 

    expect(isValid).to.be.true;
    expect(errors.name).to.equal('');
    expect(errors.email).to.equal('');
    expect(errors.password).to.equal('');

  });

  it('姓名不能為空', () => {
    const userData = { name: '', email: 'john.doe@example.com', password: '123456' };
    const isValid = validateForm(false, userData, errors);

    expect(isValid).to.be.false;
    expect(errors.name).to.equal('姓名不能為空');
  });

  it('email不能為空', () => {
    const userData = { name: 'John Doe', email: '', password: '123456' };
    const isValid = validateForm(false, userData, errors);

    expect(isValid).to.be.false;
    expect(errors.email).to.equal('Email不能為空');
  });
});
