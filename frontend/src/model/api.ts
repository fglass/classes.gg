import { Player } from "./player";

export default class Api {

    private static SERVER_URL = process.env.NODE_ENV === "production" ? "/api" : "http://localhost:5000/api"

    private static async request<T>(endpoint: string): Promise<T> {
        const response = await fetch(`${this.SERVER_URL}/${endpoint}`);
        return await response.json();
    }

    static getPlayer(username: string): Promise<Player> {
        return this.request<Player>(`player/${username}`)
    }

    static getPlayers(): Promise<Array<Player>> {
        return this.request<Array<Player>>("players")
    }
}

