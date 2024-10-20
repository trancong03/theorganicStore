import React, { useState } from "react";
import NewAddressForm from "./NewAddressForm";
import AddressCard from "../ui/AddressCard";

const AddressList = () => {
    const [addresses, setAddresses] = useState([
        { name: "Nguyễn Thị Lan", phone: "0812861704", address: "112 Cai Doi..." },
        { name: "Chí Công Trần", phone: "0812861704", address: "22 Lê Chiêu..." },
    ]);
    const [showForm, setShowForm] = useState(false);

    const handleAddAddress = (newAddress) => {
        setAddresses([...addresses, newAddress]);
    };
    const handleDeleteAddress = (indexToDelete) => {
        const updatedAddresses = addresses.filter((_, index) => index !== indexToDelete);
        setAddresses(updatedAddresses);
    };

    const handleEditAddress = (indexToEdit) => {
        console.log("Sửa địa chỉ:", indexToEdit);
    };
    return (
        <div className="mx-auto bg-white max-w-full min-h-screen p-4 flex-1 justify-between items-center">
            <h2 className="text-4xl font-bold mb-6">Sổ địa chỉ</h2>
            <div>
                {addresses.length === 0 ? (
                    <h1 className="text-gray-600 font-bold text-2xl">Chưa thêm địa chỉ</h1>
                ) : (
                    addresses.map((addr, index) => (
                        <AddressCard
                            key={index}
                            name={addr.name}
                            phone={addr.phone}
                            address={addr.address}
                            onEdit={() => handleEditAddress(index)}
                            onDelete={() => handleDeleteAddress(index)}
                        />
                    ))
                )}
            </div>
            <div className="w-full flex items-center justify-center ">
                <button
                    onClick={() => setShowForm(true)}
                    className=" w-[40%] py-3 bg-gray-800 text-white text-lg rounded-md mt-4"
                >
                    <span className="mr-2">+</span> Thêm địa chỉ mới
                </button>

                {showForm && (
                    <NewAddressForm
                        onSubmit={handleAddAddress}
                        onClose={() => setShowForm(false)}
                    />
                )}
            </div>
        </div>
    )

};

export default AddressList;
