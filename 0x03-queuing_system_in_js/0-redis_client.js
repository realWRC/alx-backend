// Connects to Redis

import { createClient } from "redis";

const client = createClient();

client.on('error', () => {
  console.error(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.quit();
