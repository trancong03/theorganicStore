import React from "react";

const Footer = () => {
  return (
    <div>
      <div className="flex flex-col sm:grid grid-cols-[3fr_1fr_1fr] gap-14 my-10 mt-40 text-sm ml-10">
        <div>
          <img
            src="https://theciu.vn/img/logo-dark.png"
            alt=""
            className="mb-5 w-32"
          />
          <p className="w-full md:w-2/3 text-gray-600">
            Lorem ipsum dolor, sit amet consectetur adipisicing elit. Ad maxime,
            voluptas non aspernatur omnis facere asperiores. Optio voluptatum
            autem, sint, dolore inventore adipisci praesentium explicabo
            distinctio libero, repellendus laboriosam fugit?
          </p>
        </div>
        <div>
          <p className="text-xl font-medium mb-5"> COMPANY</p>
          <ul className="flex flex-col gap-1 text-gray-600">
            <li>Home</li>
            <li>About us</li>
            <li>Delivery</li>
            <li>Privacy Policy</li>
          </ul>
        </div>
        <div>
          <p className="text-xl font-medium mb-5">GET IN TOUCH</p>
          <ul className="flex flex-col gap-1 text-gray-600">
            <li>Phát triển phần mềm thông minh</li>
            <li>Trần Chí Công</li>
            <li>Phạm Hồ Đăng Huy</li>
            <li>Nguyễn Thị Hằng</li>
          </ul>
        </div>
      </div>
      <div>
        <hr />
        <p className="py-5 text-sm text-center">
          Copyright2024@ theciu.vn - All Right Reserved{" "}
        </p>
      </div>
    </div>
  );
};

export default Footer;
