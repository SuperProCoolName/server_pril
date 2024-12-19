import { Module } from '@nestjs/common';
import { RecipeService } from './recipe.service';
import { RecipeController } from './recipe.controller';

@Module({
  imports: [],
  controllers: [RecipeController],
  providers: [RecipeService],
})
export class RecipeModule {}
