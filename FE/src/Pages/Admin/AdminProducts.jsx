import React, { useState } from 'react';

function AdminProducts() {
  const [products, setProducts] = useState([
    { id: 1, name: 'Product 1', price: 100, stock: 50, type: 'Type A', expiration: '2024-12-31', images: [] },
    { id: 2, name: 'Product 2', price: 200, stock: 30, type: 'Type B', expiration: '2025-01-15', images: [] },
    { id: 3, name: 'Product 3', price: 150, stock: 20, type: 'Type C', expiration: '2024-11-20', images: [] },
  ]);

  const [newProduct, setNewProduct] = useState({
    id: '',
    name: '',
    price: '',
    stock: '',
    type: '',
    expiration: '',
    images: [],
  });

  const handleAdd = () => {
    if (!newProduct.id || !newProduct.name || !newProduct.price || !newProduct.stock || !newProduct.type || !newProduct.expiration) {
      alert('Please fill in all fields.');
      return;
    }

    if (products.some((product) => product.id === newProduct.id)) {
      alert('Product ID already exists. Please use a different ID.');
      return;
    }

    const newProductData = {
      ...newProduct,
      images: newProduct.images.map((image) => URL.createObjectURL(image)),
    };

    setProducts([...products, newProductData]);
    setNewProduct({
      id: '',
      name: '',
      price: '',
      stock: '',
      type: '',
      expiration: '',
      images: [],
    });
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewProduct((prev) => ({ ...prev, [name]: value }));
  };

  const handleImageChange = (e) => {
    const files = Array.from(e.target.files);
  
    if (files.length > 4) {
      alert('Bạn chỉ được tải lên tối đa 4 hình ảnh.');
      return;
    }
  
    setNewProduct((prev) => ({ ...prev, images: files }));
  };

  const handleEdit = (id) => {
    const updatedProducts = products.map((product) =>
      product.id === id ? { ...product, name: 'Updated Product' } : product
    );
    setProducts(updatedProducts);
  };

  const handleDelete = (id) => {
    const updatedProducts = products.filter((product) => product.id !== id);
    setProducts(updatedProducts);
  };

  return (
    <div className="p-4">
      <h2 className="text-4xl font-bold text-center mb-6 bg-gradient-to-r from-blue-500 to-purple-600 text-white py-2 rounded-md shadow-lg">
        Quản lý Sản Phẩm
      </h2>
      <div className="mb-6 flex flex-wrap gap-2">
        <input
          type="text"
          name="id"
          placeholder="ID Sản Phẩm"
          value={newProduct.id}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        <input
          type="text"
          name="name"
          placeholder="Tên Sản Phẩm"
          value={newProduct.name}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        <input
          type="number"
          name="price"
          placeholder="Giá"
          value={newProduct.price}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        <input
          type="number"
          name="stock"
          placeholder="Tồn Kho"
          value={newProduct.stock}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        <input
          type="text"
          name="type"
          placeholder="Loại"
          value={newProduct.type}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        <input
          type="date"
          name="expiration"
          value={newProduct.expiration}
          onChange={handleChange}
          className="border px-2 py-1"
        />

        {/* Custom Styled File Input */}
        <div className="relative">
          <input
            type="file"
            name="image"
            accept="image/*"
            onChange={handleImageChange}
            className="absolute inset-0 opacity-0 cursor-pointer"
            multiple
          />
          <button className="bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 text-white px-4 py-2 shadow-blue-500/50 rounded-full">
            Chọn Hình Ảnh (Tối đa 4)
          </button>
        </div>

        <button
          onClick={handleAdd}
          className="bg-gradient-to-r from-teal-400 to-blue-500 hover:from-pink-500 hover:to-orange-500 text-white px-4 py-2 shadow-blue-500/50 rounded-full"
        >
          Thêm Sản Phẩm
        </button>
      </div>
      <table className="min-w-full bg-white border border-gray-300">
        <thead>
          <tr className="bg-gray-100">
            <th className="py-3 px-4 border-b text-center">ID</th>
            <th className="py-3 px-4 border-b text-center">Tên Sản Phẩm</th>
            <th className="py-3 px-4 border-b text-center">Giá</th>
            <th className="py-3 px-4 border-b text-center">Tồn Kho</th>
            <th className="py-3 px-4 border-b text-center">Loại</th>
            <th className="py-3 px-4 border-b text-center">Hạn Sử Dụng</th>
            <th className="py-3 px-4 border-b text-center">Hình Ảnh</th>
            <th className="py-3 px-4 border-b text-center">Hành Động</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product) => (
            <tr key={product.id} className="hover:bg-gray-50">
              <td className="py-3 px-4 border-b text-center">{product.id}</td>
              <td className="py-3 px-4 border-b text-center">{product.name}</td>
              <td className="py-3 px-4 border-b text-center">{product.price}</td>
              <td className="py-3 px-4 border-b text-center">{product.stock}</td>
              <td className="py-3 px-4 border-b text-center">{product.type}</td>
              <td className="py-3 px-4 border-b text-center">{product.expiration}</td>
              <td className="py-3 px-4 border-b text-center">
                {product.images.length > 0 ? (
                  <div className="flex flex-wrap justify-center gap-2">
                    {product.images.map((image, index) => (
                      <img key={index} src={image} alt={`${product.name} ${index + 1}`} className="h-16 w-16 object-cover" />
                    ))}
                  </div>
                ) : (
                  'No Images'
                )}
              </td>
              <td className="py-3 px-4 border-b text-center">
                <button
                  onClick={() => handleEdit(product.id)}
                  className="bg-yellow-500 text-white px-2 py-1 rounded-full mr-2"
                >
                  Sửa
                </button>
                <button
                  onClick={() => handleDelete(product.id)}
                  className="bg-red-500 text-white px-2 py-1 rounded-full"
                >
                  Xóa
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AdminProducts;
