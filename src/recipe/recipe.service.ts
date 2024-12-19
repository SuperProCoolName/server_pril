import { Injectable } from '@nestjs/common';
import { CreateRecipeDto } from './dto/create-recipe.dto';
import { UpdateRecipeDto } from './dto/update-recipe.dto';

@Injectable()
export class RecipeService {
  private recipes = [];
  private id = 0;

  create(createRecipeDto: CreateRecipeDto) {
    const recipe = { id: ++this.id, ...createRecipeDto };
    this.recipes.push(recipe);
    return recipe;
  }

  findAll() {
    return this.recipes;
  }

  findOne(id: number) {
    return this.recipes.find((recipe) => recipe.id === id);
  }

  update(id: number, updateRecipeDto: UpdateRecipeDto) {
    const index = this.recipes.findIndex((recipe) => recipe.id === id);
    if (index > -1) {
      this.recipes[index] = { ...this.recipes[index], ...updateRecipeDto };
      return this.recipes[index];
    }
    return null;
  }

  remove(id: number) {
    const index = this.recipes.findIndex((recipe) => recipe.id === id);
    if (index > -1) {
      return this.recipes.splice(index, 1)[0];
    }
    return null;
  }
}
