import React, { useState, useEffect } from 'react';
import ProductList from './productList';

const App = () => {
  const productData = [
    {
      Ean: 'EAN001',
      nombre_producto: 'Producto 1',
      datos_query: [
        { Market: 'Market1', normal_price: 10 },
        { Market: 'Market2', normal_price: 15 }
      ],
      markets_diferentes: new Set(['Market1', 'Market2']),
      rango_precios: [10, 15]
    },
    {
      Ean: 'EAN002',
      nombre_producto: 'Producto 2',
      datos_query: [
        { Market: 'Market2', normal_price: 15 },
        { Market: 'Market1', normal_price: 20 }
      ],
      markets_diferentes: new Set(['Market2', 'Market1']),
      rango_precios: [15, 20]
    },
    {
      Ean: 'EAN003',
      nombre_producto: 'Producto 3',
      datos_query: [
        { Market: 'Market1', normal_price: 20 },
        { Market: 'Market2', normal_price: 30 }
      ],
      markets_diferentes: new Set(['Market1', 'Market2']),
      rango_precios: [20, 30]
    },
  ];

const [products, setProducts] = useState(productData);
  const [filter, setFilter] = useState('');
  const [intervalId, setIntervalId] = useState(null);

  const applyFilter = () => {
    const filteredProducts = productData.filter((product) =>
      product.nombre_producto.toLowerCase().includes(filter.toLowerCase())
    );

    setProducts(filteredProducts);

    let index = 0;
    const id = setInterval(() => {
      setProducts((prevProducts) => {
        const updatedProducts = [...prevProducts];
        updatedProducts.splice(index, 1);
        index++;
        if (index >= updatedProducts.length) {
          clearInterval(id);
        }
        return updatedProducts;
      });
    }, 1000);

    setIntervalId(id);
  };

  useEffect(() => {
    return () => {
      if (intervalId) {
        clearInterval(intervalId);
      }
    };
  }, [intervalId]);

  const handleFilterChange = (event) => {
    setFilter(event.target.value);
  };

  return (
    <div>
      <h1>Lista de Productos</h1>
      <input
        type="text"
        placeholder="Filtrar por nombre"
        value={filter}
        onChange={handleFilterChange}
      />
      <button onClick={applyFilter}>Aplicar Filtro</button>
      <ProductList products={products} />
    </div>
  );
};
export default App;



//   const [products, setProducts] = useState(productData);
//   const [filter, setFilter] = useState('');
//   const [index, setIndex] = useState(0);
//   const [intervalId, setIntervalId] = useState(null);

//   const applyFilter = () => {
//     const filteredProducts = productData.filter((product) =>
//       product.nombre_producto.toLowerCase().includes(filter.toLowerCase())
//     );

//     setIndex(0);
//     const id = setInterval(() => {
//       setProducts((prevProducts) => {
//           const updatedProducts = [...prevProducts];
//           updatedProducts.splice(index, 1);
//           setIndex((prevIndex) => {
//             const nextIndex = prevIndex + 1;
//           if (nextIndex >= prevProducts.length) {
//             clearInterval(id);
//           }
//           return nextIndex;
//         });
//         return updatedProducts
//       });
//     }, 1000);

//     setIntervalId(id);
//   };

//   useEffect(() => {
//     return () => {
//       if (intervalId) {
//         clearInterval(intervalId);
//       }
//     };
//   }, [intervalId]);
  
//   const handleFilterChange = event => {
//     setFilter(event.target.value);
//   };

//   return (
//     <div>
//       <h1>Lista de Productos</h1>
//       <input
//         type="text"
//         placeholder="Filtrar por nombre"
//         value={filter}
//         onChange={handleFilterChange}
//       />
//       <button onClick={applyFilter}>Aplicar Filtro</button>
//       <ProductList products={products} />
//     </div>
//   );
// };


