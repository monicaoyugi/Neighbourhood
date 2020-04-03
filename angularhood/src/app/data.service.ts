import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Hood } from './hood.model';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  apiUrl = 'http://127.0.0.1:8000/api/v1/hoods/';

  constructor(private _http:HttpClient) { }

  getHoods(){
    return this._http.get<Hood[]>(this.apiUrl);
  }
}
