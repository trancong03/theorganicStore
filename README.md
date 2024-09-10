# **Xây dựng hệ thống bán hàng thời trang**

**Mô tả:**  
Dự án xây dựng hệ thống quản lý bán hàng thời trang, áp dụng AI để gợi ý sản phẩm khi người dùng đặt hàng và phân cụm khách hàng để tặng khuyến mãi. Hệ thống bao gồm 2 nền tảng chính là WebForm (ReactJS & NodeJS) và WinForm (C#).

## **Thành viên nhóm**

| Thành viên         | Vai trò          |
|--------------------|------------------|
| Trần Chí Công      | Nhóm trưởng      |
| Phạm Hồ Đăng Huy   | Thành viên       |
| Nguyễn Thị Hằng    | Thành viên       |

## **Công nghệ sử dụng**

- **Database:** Neo4j
- **WebForm:**
  - **Front End:** ReactJS
  - **Back End:** NodeJS
- **WinForm:** C#
- **AI:** K-Means clustering

## **Mô tả nền tảng**

### **1. WinForm (C#)**

Ứng dụng quản lý dành cho Admin với các chức năng chính:

- **Quản lý sản phẩm:** Thêm, sửa, xóa và quản lý thông tin sản phẩm.
- **Quản lý nhà cung cấp:** Quản lý danh sách nhà cung cấp và lịch sử giao dịch.
- **Quản lý khách hàng:** Quản lý thông tin và phân cụm khách hàng thân thiết (AI - K-Means).
- **Báo cáo thống kê:** Xây dựng các báo cáo doanh thu, sản phẩm bán chạy, tình hình kho hàng.
- **Quản lý nhập hàng:** Theo dõi và quản lý quá trình nhập hàng từ nhà cung cấp.
- **Quản lý hóa đơn:** Tạo, lưu trữ và xuất hóa đơn sau khi khách hàng mua hàng.
- **Quản lý tài khoản:** Quản lý người dùng, phân quyền và bảo mật hệ thống.
- **Quản lý khuyến mãi:** Sử dụng AI để phân cụm khách hàng và gợi ý khuyến mãi phù hợp.

### **2. WebForm (ReactJS & NodeJS)**

Nền tảng web cho người dùng với các
