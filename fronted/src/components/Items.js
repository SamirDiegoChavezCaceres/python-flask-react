

import React, {useState, useEffect} from 'react';

const API = process.env.REACT_APP_API;
const prefix = "v1"

export const Items = () => {

    const [id, setId] = useState("")
    const [codebar, setCodebar] = useState("")
    const [name, setName] = useState("")
    const [description, setDescription] = useState("")
    const [price, setPrice] = useState("")
    const [stock, setStock] = useState("")
    const [state, setState] = useState("")
    const [items, setItems] = useState([])
    const [editing, setEditing] = useState(false)
    
    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!editing) {
            const response = await fetch(`${API}/${prefix}/item/`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    codebar: codebar,
                    name: name,
                    description: description,
                    price: parseFloat(price),
                    stock: parseInt(stock),
                })
            })
            const data = await response.json()
            console.log(data)
        } else {
            const response = await fetch(`${API}/${prefix}/item/`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    item_id: id,
                    codebar: codebar,
                    name: name,
                    description: description,
                    price: parseFloat(price),
                    stock: parseInt(stock),
                    state: state
                })
            })
            const data = await response.json()
            document.getElementById('save-button').innerText = "Save"
            document.getElementById('cancel-button').style.display = "none"
            setEditing(false)
            console.log(data)
        }
        await getItems()
        clearForm()
    }


    const getItems = async () => {
        const response = await fetch(`${API}/${prefix}/items/`)
        const data = await response.json()
        setItems(data.items)
    }


    const deleteItem = async (id) => {
        const user_response = window.confirm("Are you sure you want to delete it?")
        if (user_response) {
            const response = await fetch(`${API}/${prefix}/item/`, {
                method: "DELETE",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    item_id: id
                })
            })
            const data = await response.json()
            console.log(data)
        }
        await getItems()
    }


    const editItem = async (id) => {
        const item = await getItem(id)
        setId(item.item_id)
        setCodebar(item.codebar)
        setName(item.name)
        setDescription(item.description)
        setPrice(item.price)
        setStock(item.stock)
        setState(item.state)
        // show cancel button
        document.getElementById('cancel-button').style.display = "block"
        document.getElementById('save-button').innerText = "Update"
        setEditing(true)
    }


    const getItem = async (id) => {
        const response = await fetch(`${API}/${prefix}/item/?item_id=${id}`)
        return response.json()
    }


    const cancelEdit = () => {
        clearForm()
        // hide cancel button
        document.getElementById('cancel-button').style.display = "none"
        document.getElementById('save-button').innerText = "Save"
    }


    const deactivateItem = async (id) => {
        const response = await fetch(`${API}/${prefix}/item/deactivate/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                item_id: id
            })
        })
        const data = await response.json()
        console.log(data)
        await getItems()
    }


    const activateItem = async (id) => {
        const response = await fetch(`${API}/${prefix}/item/activate/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                item_id: id
            })
        })
        const data = await response.json()
        console.log(data)
        await getItems()
    }


    const clearForm = () => {
        setId("")
        setCodebar("")
        setName("")
        setDescription("")
        setPrice("")
        setStock("")
        setState("")
    }


    useEffect(() => {
        getItems()
        // hide cancel button
        document.getElementById('cancel-button').style.display = "none"
    }, [])


    return (
        <div className="row">
            <div className="col-md-4">
                <form onSubmit={handleSubmit} className='card card-body'>
                    <div className="form-group">
                        <input
                            type="text"
                            onChange={(e) => setId(e.target.value)}
                            value={id}
                            className='form-control'
                            placeholder='ID'
                            disabled={true}
                        />
                    </div>
                    <div className="form-group">
                        <input
                            type="text"
                            onChange={(e) => setCodebar(e.target.value)}
                            value={codebar}
                            className='form-control'
                            placeholder='Codebar'
                            autoFocus
                        />
                    </div>
                    <div className="form-group">
                        <input
                            type="text"
                            onChange={(e) => setName(e.target.value)}
                            value={name}
                            className='form-control'
                            placeholder='Name'
                        />
                    </div>
                    <div className="form-group">
                        <input
                            type="text"
                            onChange={(e) => setDescription(e.target.value)}
                            value={description}
                            className='form-control'
                            placeholder='Description'
                        />
                    </div>
                    <div className="form-group">
                        <input
                            type="text"
                            onChange={(e) => setPrice(e.target.value)}
                            value={price}
                            className='form-control'
                            placeholder='Price'
                        />
                    </div>
                    <div className="form-group">
                        <input
                            type="text"
                            onChange={(e) => setStock(parseFloat(e.target.value))}
                            value={stock}
                            className='form-control'
                            placeholder='Stock'
                        />
                    </div>
                    <div className="form-group">
                        <input
                            type="text"
                            onChange={(e) => setState(parseInt(e.target.value))}
                            value={state}
                            className='form-control'
                            placeholder='State'
                            disabled={true}
                        />
                    </div>
                    <button 
                        className="btn btn-primary btn-block"
                        id='save-button'
                    >
                        Save
                    </button>
                </form>
                <div style={{marginTop: "20px", display: "flex", justifyContent: "center",}}>
                    <button 
                        className="btn btn-secondary btn-block"
                        id='cancel-button'
                        onClick={() => cancelEdit()}
                    >
                        Cancel
                    </button>
                </div>
            </div>
            <div className="col-md-6">
                <table className="table table-striped">
                    <thead>
                        <tr>
                            <th>Codebar</th>
                            <th>Name</th>
                            <th>Description</th>
                            <th>Price</th>
                            <th>Stock</th>
                            <th>State</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {
                            items.map((item) => (
                                <tr key={item.item_id}>
                                    <td>{item.codebar}</td>
                                    <td>{item.name}</td>
                                    <td>{item.description}</td>
                                    <td>{item.price}</td>
                                    <td>{item.stock}</td>
                                    { item.state ?
                                        <td>Active</td> : <td>Inactive</td>
                                    }
                                    <td>
                                        <button 
                                            className="btn btn-secondary btn-sm btn-block"
                                            onClick={() => editItem(item.item_id)}
                                        >
                                            Edit
                                        </button>
                                        <button 
                                            className="btn btn-danger btn-sm btn-block"
                                            onClick={() => deleteItem(item.item_id)}
                                        >
                                            Delete
                                        </button>
                                        { item.state ?
                                            <button
                                                className="btn btn-warning btn-sm btn-block"
                                                onClick={() => deactivateItem(item.item_id)}
                                            >
                                                Deactivate
                                            </button> :
                                            <button
                                                className="btn btn-info btn-sm btn-block"
                                                onClick={() => activateItem(item.item_id)}
                                            >
                                                Activate
                                            </button>
                                        }
                                    </td>
                                </tr>
                            ))
                        }
                    </tbody>
                </table>
            </div>
        </div>
        )
    };