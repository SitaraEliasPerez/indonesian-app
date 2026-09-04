import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:5000/api",
});

export const fetchAllWords = () => api.get("/words");
export const fetchByCategory = (category) => api.get(`/words/${category}`);

export default api;