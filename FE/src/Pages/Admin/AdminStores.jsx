import React, { useEffect, useState } from 'react';

function AdminStore() {
  const [stores, setStores] = useState([]); // Danh sách các cửa hàng
  const [newStore, setNewStore] = useState({
    name: '',
    address: '',
    email: '',
    hotline: '',
  });

  // Fetch cửa hàng từ API
  useEffect(() => {
    const fetchStores = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/get_stores/');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setStores(result.stores);
      } catch (error) {
        console.error('Error fetching stores:', error);
      }
    };

    fetchStores();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setNewStore((prev) => ({ ...prev, [name]: value }));
  };

  const handleAdd = async () => {
    if (!newStore.name || !newStore.address || !newStore.email || !newStore.hotline) {
      alert('Please fill in all fields.');
      return;
    }

    try {
      const response = await fetch('http://127.0.0.1:8000/api/add_store/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(newStore),
      });

      if (!response.ok) {
        throw new Error('Failed to add store');
      }

      const addedStore = await response.json();
      setStores([...stores, addedStore]);
      setNewStore({
        name: '',
        address: '',
        email: '',
        hotline: '',
      });
    } catch (error) {
      console.error('Error adding store:', error);
    }
  };

  const handleDelete = async (id) => {
    try {
      const response = await fetch(`http://127.0.0.1:8000/api/delete_store/${id}/`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('Failed to delete store');
      }

      const updatedStores = stores.filter((store) => store.id !== id);
      setStores(updatedStores);
    } catch (error) {
      console.error('Error deleting store:', error);
    }
  };

  return (
    <div className="p-4">
      <h2 className="text-4xl font-bold text-center mb-6 bg-gradient-to-r from-blue-500 to-purple-600 text-white py-2 rounded-md shadow-lg">
        Quản lý Cửa Hàng
      </h2>

      <div className="mb-6 flex flex-wrap gap-2">
        <input
          type="text"
          name="name"
          placeholder="Tên Cửa Hàng"
          value={newStore.name}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        <input
          type="text"
          name="address"
          placeholder="Địa Chỉ"
          value={newStore.address}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          value={newStore.email}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        <input
          type="text"
          name="hotline"
          placeholder="Hotline"
          value={newStore.hotline}
          onChange={handleChange}
          className="border px-2 py-1"
        />
        
        <button
          onClick={handleAdd}
          className="bg-gradient-to-r from-teal-400 to-blue-500 hover:from-pink-500 hover:to-orange-500 text-white px-4 py-2 shadow-blue-500/50 rounded-full"
        >
          Thêm Cửa Hàng
        </button>
      </div>

      <table className="min-w-full bg-white border border-gray-300 shadow-md rounded-lg overflow-hidden">
        <thead className="bg-gray-200 text-gray-700">
          <tr>
            <th className="py-3 px-4 border-b text-center font-semibold">ID</th>
            <th className="py-3 px-4 border-b text-center font-semibold">Tên Cửa Hàng</th>
            <th className="py-3 px-4 border-b text-center font-semibold">Địa Chỉ</th>
            <th className="py-3 px-4 border-b text-center font-semibold">Email</th>
            <th className="py-3 px-4 border-b text-center font-semibold">Hotline</th>
            <th className="py-3 px-4 border-b text-center font-semibold">Hành Động</th>
          </tr>
        </thead>
        <tbody className="text-gray-600">
          {stores.map((store) => (
            <tr key={store.id} className="hover:bg-gray-50 transition-colors duration-150">
              <td className="py-3 px-4 border-b text-center">{store.id}</td>
              <td className="py-3 px-4 border-b text-center">{store.name}</td>
              <td className="py-3 px-4 border-b text-center">{store.address}</td>
              <td className="py-3 px-4 border-b text-center">{store.email}</td>
              <td className="py-3 px-4 border-b text-center">{store.hotline}</td>
              <td className="py-3 px-4 border-b text-center">
                <button
                  onClick={() => handleDelete(store.id)}
                  className="bg-red-500 text-white px-3 py-1 rounded hover:bg-red-600 transition duration-200"
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

export default AdminStore;
