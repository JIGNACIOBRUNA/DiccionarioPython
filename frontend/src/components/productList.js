import React from 'react';

const ProductList = ({ products }) => {
  return (
    <div>
      {products.map(product => (
        <div key={product.Ean}>
          <h3>{product.nombre_producto}</h3>
          <p>Rango de precios: {product.rango_precios.join(' - ')}</p>
          <p>Mercados diferentes: {Array.from(product.markets_diferentes).join(', ')}</p>
          <hr />
        </div>
      ))}
    </div>
  );
};

export default ProductList;
