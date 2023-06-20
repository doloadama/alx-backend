import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();

const listProducts = [
  {
    itemId: 1,
    itemName: 'Suitcase 250',
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: 'Suitcase 450',
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: 'Suitcase 650',
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: 'Suitcase 1050',
    price: 550,
    initialAvailableQuantity: 5,
  },
];

const getItemById = (id) => {
  return listProducts.find((item) => item.itemId === id);
};

const reserveStockById = async (itemId, stock) => {
  const setAsync = promisify(client.set).bind(client);
  await setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(`item.${itemId}`);
  return parseInt(reservedStock, 10) || 0;
};

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId, 10));

  if (item) {
    const currentQuantity = await getCurrentReservedStockById(itemId);
    res.json({ ...item, currentQuantity });
  } else {
    res.json({ status: 'Product not found' });
  }
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const { itemId } = req.params;
  const item = getItemById(parseInt(itemId, 10));

  if (!item) {
    res.json({ status: 'Product not found' });
  } else {
    const currentQuantity = await getCurrentReservedStockById(itemId);

    if (currentQuantity >= item.initialAvailableQuantity) {
      res.json({ status: 'Not enough stock available', itemId: item.itemId });
    } else {
      await reserveStockById(itemId, currentQuantity + 1);
      res.json({ status: 'Reservation confirmed', itemId: item.itemId });
    }
  }
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
