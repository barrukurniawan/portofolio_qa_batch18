const domain = require("supertest")("http://barru.pythonanywhere.com");
const expect = require("chai").expect;

describe("Scenario Login Feature", function () {
  it("Verify Success Login with valid email and password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "jokotampan900@gmail.com", password: "jokotampan900" });
      
    expect(response.body.status).to.eql('SUCCESS_LOGIN');
    expect(response.body.message).to.eql('Anda Berhasil Login');
    expect(response.body).to.include.keys("data", "message", "status", "credentials"); 
  });

  it("Verify Failed Login with invalid email and valid password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "jokotampan900", password: "jokotampan900" });
      
    // expect OUTPUT
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Cek kembali email anda');
    expect(response.body).to.include.keys("data", "message", "status"); 
  });

  it("Verify Failed Login with valid email and empty password", async function () { 
    const response = await domain 
      .post("/login")
      .send({ email: "jokotampan900@gmail.com", password: "" });
      
    // expect OUTPUT
    expect(response.body.status).to.eql('FAILED_LOGIN');
    expect(response.body.message).to.eql('Email atau Password Anda Salah');
    expect(response.body.data).to.eql("User's not found"); 
  });
});