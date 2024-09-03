import { Routes } from '@angular/router';
import { HomeComponent } from './components/home/home.component';
import { FormsComponent } from './components/forms/forms.component';
import { DisplayComponent } from './components/display/display.component';

export const routes: Routes = [
    {path: '', component: HomeComponent},
    {path: 'home', component: HomeComponent},
    {path: 'new', component: FormsComponent},
    {path: 'students', component: DisplayComponent},
    {path: '**', redirectTo: ''}
];
