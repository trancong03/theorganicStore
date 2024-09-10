# **🛍️ Xây dựng hệ thống bán hàng thời trang**

**Mô tả:**  
Dự án xây dựng hệ thống quản lý bán hàng thời trang, áp dụng AI để gợi ý sản phẩm khi người dùng đặt hàng và phân cụm khách hàng để tặng khuyến mãi. Hệ thống bao gồm 2 nền tảng chính là WebForm (ReactJS & NodeJS) và WinForm (C#).

## **👨‍👩‍👧‍👦 Thành viên nhóm**

| Thành viên         | Vai trò          |
|--------------------|------------------|
| Trần Chí Công      | Nhóm trưởng      |
| Phạm Hồ Đăng Huy   | Thành viên       |
| Nguyễn Thị Hằng    | Thành viên       |

## **🛠️ Công nghệ sử dụng**

- **🗄️ Database:** Neo4j
- **💻 WebForm:**
  - **Frontend:** ReactJS
  - **Backend:** NodeJS
- **🖥️ WinForm:** C#
- **🤖 AI:** K-Means clustering

## **📋 Mô tả nền tảng**

### **1. 🖥️ WinForm (C#)**

Ứng dụng quản lý dành cho Admin với các chức năng chính:

- **📦 Quản lý sản phẩm:** Thêm, sửa, xóa và quản lý thông tin sản phẩm.
- **🤝 Quản lý nhà cung cấp:** Quản lý danh sách nhà cung cấp và lịch sử giao dịch.
- **👥 Quản lý khách hàng:** Quản lý thông tin và phân cụm khách hàng thân thiết (AI - K-Means).
- **📊 Báo cáo thống kê:** Xây dựng các báo cáo doanh thu, sản phẩm bán chạy, tình hình kho hàng.
- **📥 Quản lý nhập hàng:** Theo dõi và quản lý quá trình nhập hàng từ nhà cung cấp.
- **🧾 Quản lý hóa đơn:** Tạo, lưu trữ và xuất hóa đơn sau khi khách hàng mua hàng.
- **🔐 Quản lý tài khoản:** Quản lý người dùng, phân quyền và bảo mật hệ thống.
- **🎁 Quản lý khuyến mãi:** Sử dụng AI để phân cụm khách hàng và gợi ý khuyến mãi phù hợp.

### **2. 🌐 WebForm (ReactJS & NodeJS)**

#### **Frontend (ReactJS)**

- **🛒 Đặt sản phẩm:** Người dùng duyệt và đặt mua trực tuyến.
- **📦 Theo dõi đơn hàng:** Theo dõi trạng thái đơn hàng.
- **❌ Hủy đơn hàng:** Hủy trước khi vận chuyển.
- **🔍 Xem sản phẩm:** AI gợi ý sản phẩm dựa trên lịch sử mua hàng.
- **💬 Feedback sản phẩm:** Đánh giá và phản hồi sản phẩm.

#### **Backend (NodeJS)**

- **🗄️ API:** Cung cấp các API để kết nối với Frontend và cơ sở dữ liệu.
- **🔑 Authentication:** Quản lý xác thực và phân quyền người dùng.
- **📊 Xử lý dữ liệu:** Tương tác với cơ sở dữ liệu Neo4j và xử lý dữ liệu sản phẩm, khách hàng, đơn hàng.

## **📌 Yêu cầu chức năng**

### **WinForm (C#)**
- Quản lý các đối tượng: sản phẩm, nhà cung cấp, khách hàng, khuyến mãi.
- Phân tích và báo cáo dữ liệu doanh thu, sản phẩm.
- Sử dụng K-Means để phân cụm khách hàng.

### **WebForm (ReactJS & NodeJS)**
- Quản lý giao hàng, đặt và theo dõi đơn hàng.
- Gợi ý sản phẩm sử dụng AI.
- Feedback sản phẩm.

## **🚀 Cài đặt**

### **Yêu cầu**

#### **WebForm**
- Node.js 14.x
- ReactJS 17.x
- Neo4j

#### **WinForm**
- .NET Framework 4.8
- Neo4j

### **Cài đặt WebForm**
```bash

