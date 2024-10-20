import React, { useEffect, useState } from "react";
import NewAddressForm from "./NewAddressForm";
import AddressCard from "../ui/AddressCard";
import { useCart } from "../context/CardContext";

const AddressList = () => {
    const { address } = useCart();
    const [addresses, setAddresses] = useState(address || []);
    const [showForm, setShowForm] = useState(false);

    
    const handleDeleteAddress = (indexToDelete) => {
        const updatedAddresses = addresses.filter((_, index) => index !== indexToDelete);
        setAddresses(updatedAddresses);
    };

    
    return (
        <div className="mx-auto bg-white max-w-full min-h-screen p-4 flex-1 justify-between items-center">
            <h2 className="text-4xl font-bold mb-6">Sổ địa chỉ</h2>
            <div>
                {address.length === 0 ? (
                    <h1 className="text-gray-600 font-bold text-2xl">Chưa thêm địa chỉ</h1>
                ) : (
                    address.map((addr, index) => (
                        <AddressCard
                            key={index}
                            name={addr.RecipientName}
                            phone={addr.PhoneNumber}
                            address={addr.DeliveryAddress}
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
                        onClose={() => setShowForm(false)}
                    />
                )}
            </div>
        </div>
    )

};

export default AddressList;
