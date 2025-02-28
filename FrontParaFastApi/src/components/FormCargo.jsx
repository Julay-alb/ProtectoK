import React from 'react';
import axiosInstance from '../api/axioInstance';


const cargarButton = async (e) => {
    e.preventDefault();
    const nombre_cargo = document.querySelector("#nombre_cargo").value;
    const salario = document.querySelector("#salario").value;

    const nuevoRegistro = {
      nombre_cargo,
      salario
    }
    console.log(nuevoRegistro)
    try {
      const response =  await axiosInstance.post("http://localhost:8000/cityPark_crea_cargo", nuevoRegistro);
      console.log("el nuevo registro fue un exito..." , nuevoRegistro)
      
    } catch (error) {
      if (error.response) {
        console.error("Error del servidor:", error.response.data);
      } else {
        console.error("Error de la solicitud:", error.message);
      }

    }
}

const FormCargo = () => {
  return (
    <>
    <div className='container'>

      <div className="containerForm">
        <h2>Formulario cargo</h2>
        <form>
            <fieldset>
              <label htmlFor="nombre_cargo">Nombre del cargo</label>
              <input type="text" id='nombre_cargo' required />  
            </fieldset>          
            <fieldset>
              <label htmlFor="salario">Salario</label>
              <input type="text" id='salario' required />
            </fieldset>
            <button type='submit' onClick={cargarButton}>Cargar</button>
        </form>
      </div>
    </div>
    </>
  )
}

export default FormCargo